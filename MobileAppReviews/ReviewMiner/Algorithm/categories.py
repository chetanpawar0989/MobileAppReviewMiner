

__author__ = 'Viral'

class categories(object):
    '''
    Base class for all the categories and its common attributes
    '''
    rating = 0
    category = ""
    total_score = 0
    review_tags = []
    title_tags = []
    review_hit_tags = []
    title_hit_tags = []
#    final_list = []
    individual_review_list = []
    individual_review_tags = []
    individual_review_score = 0
    individual_review_title_tags = []
    individual_review_tags_list = []
    individual_review_score_list = 0
    individual_review_title_tags_list = []
    review_line_count = 0
    category_title = ""
    review_word = ""
    title_word = ""
    string_length = 0
    score = 0
    criteria_word = ""
    title_single_word = ""
    temp_string = ""
    review_line = ""

    #
    #
    def __int__(self):
        '''
        Constructor
        '''
        individual_review_list = []

    #     self.category = ""
    #     self.total_score = 0
    #     self.review_tags = []
    #     self.title_tags = []
    #     self.review_hit_tags = []
    #     self.title_hit_tags = []
    #     self.final_list = []
    #     self.individual_review_tags = []
    #     self.individual_review_list = []
    #     self.individual_review_score = 0
    #     self.individual_review_title_tags = []
    #     self.review_line_count = 0
    #     self.category_title = ""
    #     self.review_word = ""
    #     self.string_length = 0
    #     self.score = 0
    #     self.criteria_word = ""
    #     self.title_single_word = ""
    #     self.temp_string = ""

    def resetValues(self):
        '''
        resets all the attributes
        :return: nothing
        '''
        self.category = ""
        self.total_score = 0
        self.review_tags = []
        self.title_tags = []
        self.review_hit_tags = []
        self.title_hit_tags = []
        self.category_title = ""
        self.review_word = ""
        self.string_length = 0
        self.score = 0
        self.criteria_word = ""
        self.title_single_word = ""
        self.temp_string = ""
        self.review_line = ""


    def check_for_title_tags(self):
        '''
        Checks for stop
        :return: nothing
        '''

        #categories.title_single_word = categories.title_word.lower().replace('\'','')


        categories.title_single_word = categories.title_word.lower()
        categories.string_length = len(categories.criteria_word)
        if categories.criteria_word != "":

            if categories.criteria_word in categories.title_single_word and categories.criteria_word[0:categories.string_length] == categories.title_single_word[0:categories.string_length]:
                 self.title_hit_tags.append(categories.title_word)
                 self.total_score += int(categories.score)

            #     categories.individual_review_tags.append(categories.title_word)
             #    categories.individual_review_score += categories.score



    def check_for_review_tags(self):
        if categories.criteria_word != "":
            categories.temp_string = str(categories.review_word).lower().replace('\'','')
            categories.string_length = len(categories.criteria_word)
            if categories.criteria_word in categories.temp_string and categories.criteria_word[0:categories.string_length] == categories.temp_string[0:categories.string_length]:

                self.review_hit_tags.append(categories.review_word)

                self.total_score += int(categories.score)

               # categories.individual_review_tags.append(categories.review_word)
               # categories.individual_review_score += categories.score

    def populate_initial_review_list(self):
        categories.individual_review_score += self.total_score
        categories.individual_review_tags.append(self.review_hit_tags)
        categories.individual_review_title_tags.append(self.title_hit_tags)