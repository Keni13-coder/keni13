# def DNA_strand(dna):
#     dici = {
#         "G":"C",
#         "T":"A",
#         "C":"G",
#         "A":"T"
#     }
#     return "".join([dici[i] for i in dna])







def DNA_strand(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))

print(DNA_strand("GTAT"))