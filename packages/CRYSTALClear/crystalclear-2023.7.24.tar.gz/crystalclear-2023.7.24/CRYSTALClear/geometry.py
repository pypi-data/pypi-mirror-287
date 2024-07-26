"""
Basic methods to manipulate pymatgen geometries
"""
def rotate_lattice(struc, rot):
    """
    Geometries generated by ``base.crysout.GeomBASE`` might be rotated.
    Rotate them back to make them consistent with geometries in output.

    .. math::
        \mathbf{L}_{crys} = \mathbf{L}_{pmg}\mathbf{R}

    :math:`\mathbf{R}` is the rotation matrix.

    Args:
        struc (Structure): Pymatgen structure
        rot (array): 3\*3 numpy array, rotation matrix.

    Returns:
        struc_new (Structure): Pymatgen structure
    """
    from pymatgen.core.lattice import Lattice
    from pymatgen.core.structure import Structure
    import numpy as np

    latt_mx = struc.lattice.matrix @ rot
    latt = Lattice(latt_mx, pbc=struc.pbc)
    spec = list(struc.atomic_numbers)
    coord = struc.frac_coords.tolist()
    struc_new = Structure(lattice=latt, species=spec, coords=coord, coords_are_cartesian=False)

    return struc_new


def refine_geometry(struc, **kwargs):
    """
    Get refined geometry. Useful when reducing the cell to the irrducible
    one. 3D only.

    Args:
        struc (Structure): Pymatgen structure
        **kwargs: Passed to Pymatgen `SpacegroupAnalyzer <https://pymatgen.org/pymatgen.symmetry.html#pymatgen.symmetry.analyzer.SpacegroupAnalyzer>`_ object.
    Returns:
        sg (int): Space group number
        struc5 (Structure): Irrducible structure that is consistent with
            International Crystallographic Table
        latt (list): minimal set of crystallographic cell parameters
        natom_irr (int): number of irrducible atoms
        atom (list): natom\*4 array. 1st element: atomic number; 2-4:
            fractional coordinates
    """
    from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
    import numpy as np

    ndimen = struc.pbc.count(True)
    if ndimen < 3:
        raise Exception('This method is for 3D systems only.')

    analyzer = SpacegroupAnalyzer(struc, **kwargs)
    # Analyze the refined geometry
    struc2 = analyzer.get_refined_structure()
    analyzer2 = SpacegroupAnalyzer(struc2, **kwargs)
    struc3 = analyzer2.get_primitive_standard_structure()
    analyzer3 = SpacegroupAnalyzer(struc3, **kwargs)

    struc4 = analyzer3.get_symmetrized_structure()
    struc5 = analyzer3.get_refined_structure()
    sg = analyzer3.get_space_group_number()

    latt = []
    if sg >= 1 and sg < 3:  # trilinic
        for i in ['a', 'b', 'c', 'alpha', 'beta', 'gamma']:
            latt.append(getattr(struc5.lattice, i))
    elif sg >= 3 and sg < 16:  # monoclinic
        for i in ['a', 'b', 'c', 'beta']:
            latt.append(getattr(struc5.lattice, i))
    elif sg >= 16 and sg < 75:  # orthorhombic
        for i in ['a', 'b', 'c']:
            latt.append(getattr(struc5.lattice, i))
    elif sg >= 75 and sg < 143:  # tetragonal
        for i in ['a', 'c']:
            latt.append(getattr(struc5.lattice, i))
    elif sg >= 143 and sg < 168:  # trigonal, converted to hexagonal
        struc6 = analyzer3.get_conventional_standard_structure()
        analyzer4 = SpacegroupAnalyzer(struc6, **kwargs)
        struc4 = analyzer4.get_symmetrized_structure()
        struc5 = analyzer4.get_refined_structure()
        for i in ['a', 'c']:
            latt.append(getattr(struc5.lattice, i))
    elif sg >= 168 and sg < 195:  # hexagonal
        for i in ['a', 'c']:
            latt.append(getattr(struc5.lattice, i))
    else:  # cubic
        latt.append(struc5.lattice.a)

    atom = []
    natom_irr = len(struc4.equivalent_sites)
    natom_eq = int(struc4.num_sites / natom_irr)
    for i in range(natom_irr):
        idx_eq = int(i * natom_eq)
        z = struc5.species[idx_eq].Z
        atom.append([z, struc5.sites[idx_eq].a, struc5.sites[idx_eq].b,
                     struc5.sites[idx_eq].c])

    return sg, struc5, latt, natom_irr, atom


def get_pcel(struc, smx):
    """
    Restore the supercell to primitive cell, with the origin shifted to the
    middle of lattice to utilize symmetry (as the default of CRYSTAL).

    Args:
        struc (Structure): Pymatgen structure of supercell
        smx (array): 3\*3 array of supercell expansion matrix
    Returns:
        pcel (Structure): Pymatgen structure of primitive cell
    """
    from pymatgen.core.structure import Structure
    from pymatgen.core.lattice import Lattice
    import numpy as np

    ndimen = struc.pbc.count(True)
    pbc = struc.pbc
    natom = struc.num_sites

    # That forces origin back to (0.5,0.5,0.5), but makes pbc to be 3D
    struc.make_supercell([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    shrink_mx = np.linalg.inv(smx)
    scel_mx = struc.lattice.matrix
    all_species = list(struc.atomic_numbers)
    # Shift origin to (0,0,0), consistent with CRYSTAL
    all_coords = struc.cart_coords
    for i in range(natom):
        for j in range(ndimen):
            all_coords[i, 0:ndimen] -= 0.5 * scel_mx[j, 0:ndimen]

    pcel_mx = shrink_mx @ scel_mx
    pcel_latt = Lattice(pcel_mx, pbc=pbc)
    # Fractional coords of pcel: Both periodic and no periodic sites
    all_coords = all_coords @ np.linalg.inv(pcel_mx)
    pcel_coords = []
    pcel_species = []
    for i, coord in enumerate(all_coords.round(12)): # Slightly reduce the accuracy
        if np.any(coord[0:ndimen] >= 0.5) or np.any(coord[0:ndimen] < -0.5):
            continue
        else:
            pcel_coords.append(coord)
            pcel_species.append(all_species[i])

    # For low dimen systems, this restores the non-periodic vecter length
    pcel = Structure(lattice=pcel_latt, species=pcel_species,
                     coords=pcel_coords, coords_are_cartesian=False)
    return pcel


def get_scel(struc, smx):
    """
    Get the supercell from primitive cell, with the origin shifted to the
    middle of lattice to utilize symmetry (as the default of CRYSTAL).

    Args:
        struc (Structure): Pymatgen structure of supercell
        smx (array): 3\*3 array of supercell expansion matrix
    Returns:
        scel (Structure): Pymatgen structure of supercell
    """
    from pymatgen.core.structure import Structure
    from pymatgen.core.lattice import Lattice

    ndimen = struc.pbc.count(True)
    pbc = struc.pbc
    natom = struc.num_sites

    struc.make_supercell(smx)
    scel_mx = struc.lattice.matrix
    all_species = list(struc.atomic_numbers)
    # Shift origin to (0,0,0), consistent with CRYSTAL
    all_coords = struc.cart_coords
    for i in range(natom):
        for j in range(ndimen):
            all_coords[i, 0:ndimen] -= 0.5 * scel_mx[j, 0:ndimen]

    scel_latt = Lattice(struc.lattice.matrix, pbc=pbc)

    scel = Structure(lattice=scel_latt, species=all_species,
                     coords=all_coords, coords_are_cartesian=True)
    return scel


def get_sg_symmops(struc, **kwargs):
    """
    Get space group number and corresponding symmetry operations. To keep
    consistency with International Crystallographic Table, refined geometry
    is suggested.

    Args:
        struc (Structure): Pymatgen Structure object.
        **kwargs: Passed to Pymatgen SpacegroupAnalyzer object.
    Returns:
        sg (int): Space group number
        n_symmops (int): number of symmetry operations
        symmops (array): n_symmops\*4\*3 array of symmetry operations
    """
    from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
    import numpy as np

    sg = SpacegroupAnalyzer(struc, **kwargs).get_space_group_number()
    all_symmops = SpacegroupAnalyzer(struc, **kwargs).get_symmetry_operations(cartesian=True)
    symmops = []
    ops_tmp = []
    n_symmops = 0
    # For symmetry operations with same rotation matrix, save the one with 0
    # tranlation vector.
    for symmop in all_symmops:
        if n_symmops == 0:
            n_symmops += 1
            symmops.append(np.vstack([symmop.rotation_matrix, symmop.translation_vector]))
            ops_tmp = [symmop]
        else:
            save = None
            for nop, op in enumerate(ops_tmp):
                if np.array_equal(op.rotation_matrix, symmop.rotation_matrix):
                    if np.all(op.translation_vector == 0.):
                        save = False
                        break
                    else:
                        save = True
                        save_id = nop
                        break
                else:
                    continue

            if save == True:
                symmops[save_id] = np.vstack([symmop.rotation_matrix, symmop.translation_vector])
                ops_tmp[save_id] = symmop
            elif save == None:
                symmops.append(np.vstack([symmop.rotation_matrix, symmop.translation_vector]))
                ops_tmp.append(symmop)
                n_symmops += 1
            else:
                continue

    symmops = np.reshape(np.array(symmops, dtype=float), [n_symmops, 4, 3])

    return sg, n_symmops, symmops

def Miller_norm(struc, miller, d=1.0):
    """
    Find the norm vector of a specified Miller plane

    Args:
        struc (Structure): Pymatgen Structure object.
        miller (array | list): 3\*1 list of Miller index
        d (fload): Length of norm vector

    Returns:
        vec (array): 3\*1 norm vector, normalized to 1.
    """
    import numpy as np

    zeros = np.argwhere(abs(miller) < 1)
    if len(zeros) == 0:
        vec1 = np.array([1/miller[0], 0, 0]) - np.array([0, 0, 1/miller[2]])
        vec2 = np.array([0, 1/miller[1], 0]) - np.array([0, 0, 1/miller[2]])
        vec1 = np.dot(vec1, struc.lattice.matrix)
        vec2 = np.dot(vec2, struc.lattice.matrix)
        vec = np.cross(vec1, vec2)
    elif len(zeros) == 1:
        if zeros[0][0] == 0:
            vec1 = [1, 0, 0]
            vec2 = np.array([0, 1/miller[1], 0]) - np.array([0, 0, 1/miller[2]])
        elif zeros[0][0] == 1:
            vec1 = np.array([1/miller[0], 0, 0]) - np.array([0, 0, 1/miller[2]])
            vec2 = [0, 1, 0]
        else:
            vec1 = [0, 0, 1]
            vec2 = np.array([1/miller[0], 0, 0]) - np.array([0, 1/miller[1], 0])
        vec1 = np.dot(vec1, struc.lattice.matrix)
        vec2 = np.dot(vec2, struc.lattice.matrix)
        vec = np.cross(vec1, vec2)
    else:
        if zeros[0][0] == 0 and zeros[1][0] == 1:
            vec = np.array([0., 0., 1.])
        elif zeros[0][0] == 0 and zeros[1][0] == 2:
            vec = np.array([0., 1., 0.])
        else:
            vec = np.array([1., 0., 0.])
        vec = np.dot(vec, struc.lattice.matrix)

    vec = vec / np.linalg.norm(vec) * d
    return vec
