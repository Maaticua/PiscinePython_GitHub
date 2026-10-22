import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """ affiche la shepe en 2d, tronque, print la nouvelle"""

    if not isinstance(family, list): #check type
        raise TypeError("family must be a list")

    if len(family) == 0: #check empty
        raise ValueError("family must not be empty")

    ref_size = len(family[0]) #check size all members
    for member in family:
        if not isinstance(member, list):
            raise TypeError("each member of family must be a list")
        if len(member) != ref_size:
            raise ValueError("all members of family must have the same size")
    
    np_family = np.array(family) #conversion numpy array pour attribu .cshape
    print(f"My shape is: {np_family.shape}")

    


"""
La Liste [ ] (List) : C'est un tableau dynamique totalement modifiable. Tu peux changer les valeurs, en ajouter ou en supprimer à volonté.
Équivalent C++ : std::vector.

Le Tuple ( ) (Tuple) : C'est un tableau strictement en lecture seule (immuable). Une fois créé avec ses parenthèses, il est figé en mémoire. Tu ne peux plus modifier, ajouter ou retirer des cases. C'est plus léger et très utilisé par les bibliothèques pour retourner des informations qui ne doivent pas être altérées, comme les dimensions d'une image ou d'un tableau.
Équivalent C++ : Un tableau const ou std::pair / std::tuple.

Le Dictionnaire {clé: valeur} (Dict) : Il associe une étiquette (la clé) à une donnée (la valeur), au lieu de les ranger par index numérique.
Équivalent C++ : std::map.

L'Ensemble { } (Set) : C'est une collection de valeurs uniques et non ordonnées. Si tu ajoutes cinq fois le chiffre 1, il ne sera stocké qu'une seule fois.
Équivalent C++ : std::set.
"""