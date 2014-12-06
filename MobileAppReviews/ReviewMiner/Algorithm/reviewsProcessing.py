__author__ = 'Viral'

import csv
import os
import nltk.corpus
from nltk import word_tokenize
import xlrd
import time
from datetime import datetime
from nltk.tokenize import wordpunct_tokenize
from ReviewMiner.Algorithm.categories import categories
from ReviewMiner.Algorithm.performance import performance
from ReviewMiner.Algorithm.userInterface import userInterface
from ReviewMiner.Algorithm.compatibility import compatibility
from ReviewMiner.Algorithm.request import request
from ReviewMiner.Algorithm.general import general


class ReviewsProcessing():

    all_reviews = []
    all_processed_review = []

    # individual_review_tags = []
    individual_review_list_final = []
    # individual_review_score = 0
    # individual_review_title_tags = []

    reviews = []
    tokenized = []
    imp_words = []
    rating_level = 3
    performance_object = performance()
    userInterface_object = userInterface()
    compatibility_object = compatibility()
    general_object = general()
    request_object = request()
    category_object = categories()

    def getprocessedreviews(self):

        # get the copied file in file reader
        self.initialize_lists()
        #file2 = open('uploaded_files/ReviewMiner/Test2.csv', 'rt', encoding='utf-16')
        file2 = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploaded_files/ReviewMiner/Test2.csv'), 'rt', encoding='utf-16')
        freader = csv.reader(x.replace('\0', '') for x in file2)

        #print('csv reader done.')
        #freader.__next__()
        #print(freader.__next__())

        counter = 0
        # save the index of all the columns in dictionary
        dictOfColumns = {}
        for m in freader.__next__():
            dictOfColumns[m] = counter
            counter = counter + 1

        #print(dictOfColumns['Review Text'])

        #Get all the review data (datetime, ratings, tokenized review title, tokenized review text) in 'all_reviews' list
        #Get all the reviews in 'reviews' list
        for row in freader:
          if (row[dictOfColumns['Review Title']] or row[dictOfColumns['Review Text']]):
            if (row and row[dictOfColumns['Reviewer Language']] == 'en' and int(row[dictOfColumns['Star Rating']]) <= int(categories.rating)):
                self.reviews.append(row[dictOfColumns['Review Text']])
                d = datetime.strptime(row[dictOfColumns['Review Submit Date and Time']], '%Y-%m-%dT%H:%M:%SZ')
                self.all_reviews.append([d.strftime("%m/%d/%Y", ), row[dictOfColumns['Star Rating']],row[dictOfColumns['Review Title']].split(),
                                         row[dictOfColumns['Review Text']].split()])

        # not used currently
        #nltk.download()
        #stopwords = nltk.corpus.stopwords.words('english')

        # populating 'tokenized' list based on tokenized word in 'review' list
        for review in self.reviews:
            #print(review)
            self.tokenized.append(wordpunct_tokenize(review))

        reviews = self.tokenized




        #for x in self.tokenized:
        #   print(x)
        #     imp_words.append([word for word in x if word.lower()
        #                       not in stopwords and word.isalpha()])

        # Open the criteria
        criteria = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploaded_files/ReviewMiner/Review_Criteria.xlsx'), on_demand=True)

        review_line_count = 0
        title_word = []
        for review_line in self.all_reviews:

            self.reset_individual_review_variables()

            for name in criteria.sheet_names():
                #title_single_word = title_word.lower()
                #  print(title_single_word)
                category_total_score = 0
                sheet = criteria.sheet_by_name(name)
                request_count = 0
                hit_words_tags = []
                title_hit_tags = []
                for [category, score] in zip(sheet.col(0), sheet.col(1)):
                    categories.criteria_word = category.value
                    categories.score = score.value
                    if isinstance(categories.score, str):
                        categories.score = 0

                    # checking for title at index 2 in 'all_reviews' list
                    if self.all_reviews[review_line_count][2]:
                        for title_word in self.all_reviews[review_line_count][2]:
                            categories.title_word = title_word
                            if (name == 'Performance'):
                                self.performance_object.check_for_title_tags()
                            if (name == 'UserInterface'):
                                self.userInterface_object.check_for_title_tags()
                            if (name == 'Request'):
                                self.request_object.check_for_title_tags()
                            if (name == 'Compatibility'):
                                self.compatibility_object.check_for_title_tags()
                            if (name == 'General'):
                                self.general_object.check_for_title_tags()

                    if reviews[review_line_count]:
                        if (name == 'Request'):
                            categories.review_line = self.reviews[review_line_count]
                            self.request_object.check_for_review_tags()
                        else:
                            for review_word in self.all_reviews[review_line_count][3]:
                                categories.review_word = review_word
                                if (name == 'Performance'):
                                    self.performance_object.check_for_review_tags()
                                if (name == 'UserInterface'):
                                    self.userInterface_object.check_for_review_tags()
                                if (name == 'Compatibility'):
                                    self.compatibility_object.check_for_review_tags()
                                if (name == 'General'):
                                    self.general_object.check_for_review_tags()

            if self.performance_object.total_score != 0:
                self.performance_object.final_list.append([self.all_reviews[review_line_count],
                                                           self.performance_object.category_name,
                                                           self.performance_object.review_hit_tags
                    , self.performance_object.title_hit_tags, self.performance_object.total_score])
            self.performance_object.populate_initial_review_list()

            if self.compatibility_object.total_score != 0:
                self.compatibility_object.final_list.append([self.all_reviews[review_line_count],
                                                             self.compatibility_object.category_name,
                                                             self.compatibility_object.review_hit_tags,
                                                             self.compatibility_object.title_hit_tags,
                                                             self.compatibility_object.total_score])
            self.compatibility_object.populate_initial_review_list()

            if self.userInterface_object.total_score != 0:
                self.userInterface_object.final_list.append([self.all_reviews[review_line_count],
                                                             self.userInterface_object.category_name,
                                                             self.userInterface_object.review_hit_tags,
                                                             self.userInterface_object.title_hit_tags,
                                                             self.userInterface_object.total_score])
            self.userInterface_object.populate_initial_review_list()

            if self.request_object.total_score != 0:
                self.request_object.final_list.append([self.all_reviews[review_line_count],
                                                       self.request_object.category_name,
                                                       self.request_object.review_hit_tags,
                                                       self.request_object.title_hit_tags,
                                                       self.request_object.total_score,
                                                       " ".join(self.request_object.review_hit_tags)]
                )
            self.request_object.populate_initial_review_list()

            if self.general_object.total_score != 0:
                self.general_object.final_list.append([self.all_reviews[review_line_count],
                                                       self.general_object.category_name,
                                                       self.general_object.review_hit_tags,
                                                       self.general_object.title_hit_tags,
                                                       self.general_object.total_score])
            self.general_object.populate_initial_review_list()

            if self.category_object.individual_review_score != 0:
                self.category_object.individual_review_list.append([self.all_reviews[review_line_count],
                                                                    self.category_object.individual_review_tags,
                                                                    self.category_object.individual_review_title_tags,
                                                                    self.category_object.individual_review_score])

            review_line_count += 1
            self.performance_object.resetValues()
            self.userInterface_object.resetValues()
            self.compatibility_object.resetValues()
            self.request_object.resetValues()
            self.general_object.resetValues()
            self.category_object.resetValues()

        self.performance_object.final_list.sort(key=lambda x: x[4], reverse=True)
        #for member in self.performance_object.final_list:
        #    print(member)
        #
        #
        #    print("interface")
        self.userInterface_object.final_list.sort(key=lambda x: x[4], reverse=True)
        #for member in self.userInterface_object.final_list:
        #     print(member)
        # #
        # # #    print(compatibility)
        self.compatibility_object.final_list.sort(key=lambda x: x[4], reverse=True)
        #   for member in self.compatibility_object.final_list:
        #      print(member)
        # #
        # #
        ##     print(request)
        self.request_object.final_list.sort(key=lambda x: x[4], reverse=True)
        # for member in self.request_object.final_list:
        #     print(member)

        # #
        # #     print(general)
        self.general_object.final_list.sort(key=lambda x: x[4], reverse=True)
        #for member in self.general_object.final_list:
        #    print(member)
        self.category_object.individual_review_list.sort(key=lambda x: x[3], reverse=True)
        #for member in self.category_object.individual_review_list:
        #print(len(self.category_object.individual_review_list))

        self.all_processed_review.append([self.performance_object.final_list, self.performance_object.category_name])
        self.all_processed_review.append([self.userInterface_object.final_list, self.userInterface_object.category_name])
        self.all_processed_review.append([self.compatibility_object.final_list, self.compatibility_object.category_name])
        self.all_processed_review.append([self.general_object.final_list, self.general_object.category_name])
        self.all_processed_review.append([self.request_object.final_list, self.request_object.category_name])


        return (self.all_processed_review, self.category_object.individual_review_list)


    def reset_individual_review_variables(self):

        categories.individual_review_score = 0
        categories.individual_review_title_tags = []
        categories.individual_review_tags = []

    def  initialize_lists(self):
        self.category_object.individual_review_list = []
        self.performance_object.final_list = []
        self.userInterface_object.final_list = []
        self.compatibility_object.final_list = []
        self.request_object.final_list = []
        self.general_object.final_list = []
        self.all_processed_review = []
        self.all_reviews = []


    # individual_review_tags = []

    # individual_review_score = 0
    # individual_review_title_tags = []






