__author__ = 'Chetan'

import csv
import re
import nltk.corpus
from nltk import word_tokenize
import xlrd
import time
from datetime import datetime
from nltk.tokenize import WhitespaceTokenizer


class ReviewsProcessing:

    performance = "Performance"
    userinterface = "UserInterface"
    compatibility = "Compatibility"
    request = "Request"
    general = "General"

    performance_total = 0
    userinterface_total = 0
    compatibility_total = 0
    request_total = 0
    general_total = 0

    performance_review_tags = []
    userinterface_review_tags = []
    compatibility_review_tags = []
    request_review_tags = []
    general_review_tags = []

    performance_title_tags = []
    userinterface_title_tags = []
    compatibility_title_tags = []
    request_title_tags = []
    general_title_tags = []

    hit_words_tags = []
    title_hit_tags = []


    performance_final_list = []
    userinterface_final_list = []
    compatibility_final_list = []
    request_final_list = []
    general_final_list = []
    all_reviews = []
    all_processed_review = []

    individual_review_tags = []
    individual_review_list = []
    individual_review_score = 0
    individual_review_title_tags = []

    reviews = []
    tokenized = []
    imp_words = []
    rating_level = 3




    def __init__(self):
        self.performance = "Performance"
        self.userinterface = "UserInterface"
        self.compatibility = "Compatibility"
        self.request = "Request"
        self.general = "General"

        self.performance_total = 0
        self.userinterface_total = 0
        self.compatibility_total = 0
        self.request_total = 0
        self.general_total = 0

        self.performance_review_tags = []
        self.userinterface_review_tags = []
        self.compatibility_review_tags = []
        self.request_review_tags = []
        self.general_review_tags = []

        self.performance_title_tags = []
        self.userinterface_title_tags = []
        self.compatibility_title_tags = []
        self.request_title_tags = []
        self.general_title_tags = []

        self.hit_words_tags = []
        self.title_hit_tags = []


        self.performance_final_list = []
        self.userinterface_final_list = []
        self.compatibility_final_list = []
        self.request_final_list = []
        self.general_final_list = []
        self.all_reviews = []
        self.all_processed_review = []

        self.individual_review_tags = []
        self.individual_review_list = []
        self.individual_review_score = 0
        self.individual_review_title_tags = []

        self.reviews = []
        self.tokenized = []
        self.imp_words = []
        self.rating_level = 3


    def getprocessedreviews(self):

        file2 = open('uploaded_files/ReviewMiner/Test2.csv', 'rt', encoding='utf-16')
        freader = csv.reader(x.replace('\0', '') for x in file2)

        #print('csv reader done.')
        #freader.__next__()
        #print(freader.__next__())

        counter = 0
        dictOfColumns = {}
        for m in freader.__next__():
            dictOfColumns[m] = counter
            counter = counter + 1

        #print(dictOfColumns['Review Text'])

        for row in freader:
            if (row and row[dictOfColumns['Reviewer Language']]=='en' and int(row[dictOfColumns['Star Rating']]) <= self.rating_level):
                self.reviews.append(row[dictOfColumns['Review Text']])
                d = datetime.strptime(row[dictOfColumns['Review Submit Date and Time']],'%Y-%m-%dT%H:%M:%SZ')
                self.all_reviews.append([d.strftime("%m/%d/%Y",),row[dictOfColumns['Star Rating']],row[dictOfColumns['Review Title']].split(),row[dictOfColumns['Review Text']].split()])

        stopwords = nltk.corpus.stopwords.words('english')

        for review in self.reviews:
            #print(review)
            self.tokenized.append(WhitespaceTokenizer().tokenize(review))

        reviews = self.tokenized


       # for x in self.tokenized:
        #    print(x)
        #     imp_words.append([word for word in x if word.lower()
        #                       not in stopwords and word.isalpha()])

        criteria = xlrd.open_workbook('uploaded_files/ReviewMiner/Review_Criteria.xlsx',on_demand=True)

        review_line_count=0
        title_word = []
        for review_line in self.all_reviews:
            self.reset_individual_review_variables()

            for name in criteria.sheet_names():
                #title_single_word = title_word.lower()
              #  print(title_single_word)
                category_total_score = 0
                sheet = criteria.sheet_by_name(name)
                request_count =0
                hit_words_tags = []
                title_hit_tags = []
                for [category,score] in zip(sheet.col(0),sheet.col(1)):
                    in_string = category.value

                    if self.all_reviews[review_line_count][2]:
                        for title_word in self.all_reviews[review_line_count][2]:
                                title_single_word = title_word.lower()
                                string_length = len(in_string)
                                if in_string != "":

                                    if in_string in title_single_word and in_string[0:string_length] == title_single_word[0:string_length]:
                                        title_hit_tags.append(title_word)
                                        category_total_score += score.value


                    if reviews[review_line_count]:
                        for review_word in reviews[review_line_count]:

                            if in_string != "":
                                if (name == self.request and request_count == 0):
                                    if in_string in " ".join(reviews[review_line_count]):
                                        request_count += 1
                                        hit_words_tags.append(in_string)
                                        category_total_score += score.value

                                else:

                                    temp_string = str(review_word).lower().replace('\'','')
                                    if in_string in temp_string and in_string[0:string_length] == temp_string[0:string_length]:

                                      #  print(temp_string)
                                      #  print(in_string)
                                        hit_words_tags.append(review_word)
                                        category_total_score += score.value


                if(name == self.performance):
                        performance_total = category_total_score
                        performance_review_tags = hit_words_tags
                        performance_title_tags = title_hit_tags

                elif(name == self.userinterface):
                        userinterface_total = category_total_score
                        userinterface_review_tags = hit_words_tags
                        userinterface_title_tags = title_hit_tags
                elif(name == self.compatibility):
                        compatibility_total = category_total_score
                        compatibility_review_tags = hit_words_tags
                        compatibility_title_tags = title_hit_tags
                elif(name == self.request):
                        request_total = category_total_score
                        request_review_tags = hit_words_tags
                        request_title_tags = title_hit_tags
                elif(name == self.general):
                        general_total = category_total_score
                        general_review_tags = hit_words_tags
                        general_title_tags = title_hit_tags

                self.individual_review_score += category_total_score
                self.individual_review_tags.append(hit_words_tags)
                self.individual_review_title_tags.append(title_hit_tags)

            if performance_total != 0:
                self.performance_final_list.append([self.all_reviews[review_line_count],
                                                                 self.performance,performance_review_tags,performance_title_tags,performance_total])

            if compatibility_total != 0:
                self.compatibility_final_list.append([self.all_reviews[review_line_count],
                                                                   self.compatibility,compatibility_review_tags,compatibility_title_tags,compatibility_total])
            if userinterface_total != 0:
                self.userinterface_final_list.append([self.all_reviews[review_line_count],
                                                                   self.userinterface,userinterface_review_tags,userinterface_title_tags,userinterface_total])
            if request_total != 0:
                self.request_final_list.append([self.all_reviews[review_line_count],
                                                             self.request,request_review_tags,request_title_tags,request_total])
            if general_total != 0:
                self.general_final_list.append([self.all_reviews[review_line_count],
                                                             self.general,general_review_tags,general_title_tags,general_total])

            if self.individual_review_score!= 0:
                self.individual_review_list.append([self.all_reviews[review_line_count],
                                                                self.individual_review_tags,self.individual_review_title_tags,
                                                                self.individual_review_score])
            review_line_count += 1


        self.performance_final_list.sort(key=lambda x: x[4], reverse=True)
    ##    for member in self.performance_final_list:
     #        print(member)
    #
    #
    #    print("interface")
        self.userinterface_final_list.sort(key=lambda x: x[4], reverse=True)
    #    for member in self.userinterface_final_list:
    #        print(member)
    # #
    # # #    print(compatibility)
        self.compatibility_final_list.sort(key=lambda x: x[4], reverse=True)
    # #     for member in compatibility_final_list:
    # # #        print(member)
    # #
    # #
    # #     print(request)
        self.request_final_list.sort(key=lambda x: x[4], reverse=True)
    # #     for member in request_final_list:
    # #         print(member)
    # #
    # #     print(general)
        self.general_final_list.sort(key=lambda x: x[4], reverse=True)
    # #     for member in general_final_list:
    # #         print(member)
        self.individual_review_list.sort(key=lambda x:x[3], reverse=True)
    #    for member in self.individual_review_list:
        print(len(self.individual_review_list))

        self.all_processed_review.append([self.performance_final_list,self.performance])
        self.all_processed_review.append([self.userinterface_final_list,self.userinterface])
        self.all_processed_review.append([self.compatibility_final_list,self.compatibility])
        self.all_processed_review.append([self.general_final_list,self.general])
        self.all_processed_review.append([self.request_final_list,self.request])

        return  (self.all_processed_review,self.individual_review_list)


    def reset_individual_review_variables(self):

        self.individual_review_score = 0
        self.individual_review_title_tags = []
        self.individual_review_tags = []
