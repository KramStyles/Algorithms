def count_smileys(arr:list):
    """
    Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

    Rules for a smiling face:

    - Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
    - A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
    - Every smiling face must have a smiling mouth that should be marked with either ) or D
    No additional characters are allowed except for those mentioned.

    Valid smiley face examples: :) :D ;-D :~)
    Invalid smiley faces: ;( :> :} :]

    return the number of valid smiley faces in array/list
    """
    SMILES = [')', 'D']
    EYES = [':', ';']

    smiley = [smile for smile in arr if smile[0] in EYES and smile[-1] in SMILES]
    return len(smiley)