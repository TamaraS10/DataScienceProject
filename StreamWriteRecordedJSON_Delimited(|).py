# https://codereview.stackexchange.com/questions/44349/printing-out-json-data-from-twitter-as-a-csv
import json
import sys
import os
from datetime import date

working_directory = os.getcwd()

today = str(date.today())
filename = 'TwitterGetStream_v1_Output_' + today + '_NewsSources.json'

save_filepath = working_directory + '/' + filename
print(save_filepath)

save_filepath_output = working_directory + '/TwitterGetStream_v1_Output_201700425_NewsSources_f8d.txt'

output_file = open(save_filepath_output, 'a')
line_for_header = 'tweet_id|created_at)|place.full_name|author|author_id|retweeted|retweet_count|text'
output_file.write(line_for_header)

count_total = 0
count_with_location = 0
count_retweeted = 0
count_with_retweet_count = 0
count_with_error = 0

with open(save_filepath) as tweets_data:
    for line in tweets_data:
        data = json.loads(line)
        count_total = count_total + 1

        try:
            tweet_id = data['id']
            created_at = data['created_at']
            place = data['place']
            text = data['text'].replace('\n', '')
            author = data['user']['screen_name']
            author_id = data['user']['id_str']
            retweeted = data['retweeted']

            try:
                if data['retweeted'] != false:
                    print('not false')
                    count_retweeted = count_retweeted + 1
            except:
                print("Retweeted Error")

            try:
                if str(place) != 'None':
                    count_with_location = count_with_location + 1
                    if data.get('place'):
                        print(data['place']['full_name'])
                    else:
                        print('No Location Found')
                line_for_txt = str(tweet_id) + '|' + str(created_at) + '|' + data['place']['full_name'] + '|' + str(
                    author) + '|' + str(author_id) + '|' + str(data['retweeted']) + '|' + str(text).replace('\r',
                                                                                                            ' ') + '\n'
                # print(line_for_txt)
                output_file.write(str(line_for_txt))

            except:
                print('Place Error')





        except:
            # print('Error Tweet: ' + str(tweetid))
            count_with_error = count_with_error + 1

output_file.close()
print('File exported: ' + save_filepath_output)

print('Total Tweets Read:    ' + str(count_total))
print('Having location:      ' + str(count_with_location))
print('Retweeted:            ' + str(count_retweeted))
print('Having retweet count: ' + str(count_with_retweet_count))
print('Having error:         ' + str(count_with_error))