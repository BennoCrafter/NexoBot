# import csv
# import random
# import configs
#
#
# def read_training_defs(filename):
#     dic = {}
#     with open(filename, newline='') as pfile:
#         reader = csv.reader(pfile, delimiter=';')
#         for row in reader:
#             if row:
#                 question = row[0]
#                 answer = row[1]
#                 dic[question] = answer
#     return dic
#
#
# def get_question_math():
#     if mathe_dic:
#         questions = list(mathe_dic.keys())
#         rand_question = random.randint(1, len(questions))
#         q = questions[rand_question]
#         a = mathe_dic[q]
#         return [q, a]
#     return None
#
#
# def get_question_latin():
#     if latein_dic:
#         questions = list(latein_dic.keys())
#         rand_question = random.randint(0, len(questions)-1)
#         q = questions[rand_question]
#         a = latein_dic[q]
#         return [q, a]
#     return None
#
#
# # INIT_MODULE #
# mathe_filename = configs.mathe_filename
# latein_filename = configs.latein_filename
# mathe_dic = read_training_defs(mathe_filename)
# latein_dic = read_training_defs(latein_filename)
# # MADE BY BENNO #
