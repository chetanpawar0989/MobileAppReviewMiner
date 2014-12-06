__author__ = 'Viral'
from ReviewMiner.Algorithm.categories import categories

class request(categories):
    category_name = "Request"
    final_list = []
    def __int__(self):
        final_list = []

    def check_for_review_tags(self):
        if categories.criteria_word != "":
             if categories.criteria_word in categories.review_line:
              self.review_hit_tags.append(categories.criteria_word+".")
              self.total_score += int(categories.score)






            #   if categories.criteria_word != "":
            # categories.temp_string = str(categories.review_word).lower().replace('\'','')
            # categories.string_length = len(categories.criteria_word)
            # if categories.criteria_word in categories.temp_string and categories.criteria_word[0:categories.string_length] == categories.temp_string[0:categories.string_length]:
            #     self.review_hit_tags.append(categories.review_word)
            #     self.total_score += int(categories.score)
            #     self.individual_review_tags.append(categories.review_word)
            #     self.individual_review_score += categories.score