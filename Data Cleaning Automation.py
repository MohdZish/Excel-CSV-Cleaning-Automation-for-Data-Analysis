import pandas as pd

df = pd.read_csv(r'D:\Zishan\Programming\Python\Excel Data Cleaning Automation\data.csv')
# del df['StartDate']

df.drop(
    ['StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress', 'Duration (in seconds)', 'Finished', 'RecordedDate'],
    axis=1, inplace=True)
df.drop(['ResponseId', 'RecipientLastName', 'RecipientFirstName', 'RecipientEmail', 'ExternalReference',
         'LocationLatitude'], axis=1, inplace=True)
df.drop(['LocationLongitude', 'DistributionChannel', 'UserLanguage', 'Q17_6_TEXT', 'Q18_10_TEXT', 'Q22', 'Q23'], axis=1,
        inplace=True)

df = df[0:]
df.drop(df.index[[1]], inplace=True)

D1 = {'Q1_1': 'I rarely get irritated',
      'Q1_2': 'I keep my emotions under control.',
      'Q1_3': 'I am not easily annoyed.',
      'Q1_4': 'I feel threatened easily.',
      'Q1_5': 'I worry about things.',
      'Q2_1': 'I find it difficult to get down to work.',
      'Q2_2': 'I finish what I start.',
      'Q2_3': 'I get things done quickly.',
      'Q2_4': 'I always postpone decisions.',
      'Q3_1': 'I am not interested in other peoples problems.',
      'Q3_2': 'I feel others emotions.',
      'Q3_3': 'I inquire about others well-being.',
      'Q3_4': 'I cant be bothered with others needs.',
      'Q3_5': 'I sympathize with others feelings.',
      'Q3_6': 'I am indifferent to the feelings of others.',
      'Q4_1': 'I Keep others at a distance.',
      'Q4_2': 'I reveal little about myself.',
      'Q4_3': 'I warm up quickly to others.',
      'Q4_4': 'I show my feelings when I am happy.',
      'Q5_1': 'I am quick to understand things.',
      'Q5_2': 'I can handle a lot of information.',
      'Q5_3': 'I like to solve complex problems.',
      'Q6_1': 'I refused to believe that it has happened.',
      'Q6_2': 'I pretend that it hasnt really happened.',
      'Q6_3': 'I acted as though it hasnt even happened.',
      'Q6_4': 'I learned to live with it.',
      'Q6_5': 'I accepted that this has happened and that it cant be changed.',
      'Q6_6': 'I accepted the reality of the fact that it happened.',
      'Q7_1': 'I took additional action to feel more comfortable with distance working.',
      'Q7_2': 'I concentrated my efforts on upgrading my skills related with distance working.',
      'Q7_3': 'I did what has to be done, one step at a time, to feel comfortable with distance working.',
      'Q7_4': 'I asked people who had similar experiences what they did.',
      'Q7_5': 'I tried to get advice from someone about what to do.',
      'Q7_6': 'I talked to someone to find out more about the situation',
      'Q7_7': 'I tried to come up with a strategy about what to do.',
      'Q7_8': 'I made a plan of action.',
      'Q7_9': 'I thought hard about what steps to take.',
      'Q8_1': 'I hesitate to use digital tools at home for fear of making mistakes that I cannot correct.',
      'Q8_2': 'I feel apprehensive about using the digital tools at home.',
      'Q8_3': 'I have avoided digital tools because they are unfamiliar and somewhat intimidating to me.',
      'Q8_4': 'I have control over using technologies used for remote work when performing my work tasks.',
      'Q8_5': 'I have the resources necessary to use the technologies available to me for remote work.',
      'Q8_6': 'I have the knowledge necessary to use the technologies available to me for remote work.',
      'Q9_1': 'I work on my days off.',
      'Q9_2': 'I work after normal business hours.',
      'Q9_3': 'I work late into the night at home.',
      'Q9_4': 'Remote working has a favorable influence on my overall attitude toward my job.',
      'Q9_5': 'Remote work encourages me to do my best.',
      'Q9_6': 'I have enough authority to do my job remotely.',
      'Q9_7': 'My responsibilities are clearly defined according to remote working procedures in my company.',
      'Q9_8': 'My manager is very concerned about my welfare, I receive enough help and equipment to get the job done.',
      'Q10_1': 'I perceive distance working as an opportunity in my work.',
      'Q10_2': 'Distance working will improve my work effectiveness.',
      'Q10_3': 'I fear my personal life being invaded due to distance working.',
      'Q10_4': 'I do not know enough technologies to handle distance working satisfactorily.',
      'Q10_5': 'I need a long time to understand and use technologies to feel comfortable about distance working.',
      'Q11_1': 'I feel satisfied with the relationships I have with my colleagues while working remotely.',
      'Q11_2': 'There is someone at work I can talk to about my day to day problems of remote work if I need to.',
      'Q11_3': 'I often feel abandoned by my co-workers when I am under pressure while working remotely.',
      'Q11_4': 'I often feel alienated from my co-workers due to remote work.',
      'Q11_5': 'I experience a general sense of emptiness when I am working remotely.',
      'Q12_1': 'I approached my supervisor with suggestions for improvement.',
      'Q12_2': 'I searched for the cause of remote work problems I encounter.',
      'Q12_3': 'I changed something in my work in order to improve it.',
      'Q12_4': 'I came up with new, original ideas for handling remote work.',
      'Q12_5': 'I redesigned job tasks for greater effectiveness and efficiency.',
      'Q12_6': 'I got against established policies if it will result in meeting a broader organizational goal.',
      'Q13_1': 'How would you rate your satisfaction with distance working. - Lowest to highest',
      'Q14_1': 'All in all, I am satisfied with virtual work.',
      'Q14_2': 'Virtual work allows me to perform my job better than I ever could when I worked in the office.',
      'Q14_3': 'If I were now given the choice to return to office environment, I would be very unlikely to do so.',
      'Q14_4': 'Since I started working virtually, I have been able to balance my job and personal life.',
      'Q14_5': 'Since I started working virtually, my productivity at work has increased.',
      'Q15': 'What is your gender?',
      'Q16': 'What is your age?',
      'Q17': 'What is your education level?',
      'Q18': 'What is your nationality?',
      'Q19_1': 'How would you rate your experience with digital technology?',
      'Q20_1': 'Please tell us whether you are still in confinement with respect to your current work location?',
      'Q21_1': 'What is the context of your current work situation in terms of remote or physical?'
      }

for k in D1.keys():
    df.at[0, k] = D1[k]

print(df)

import numpy as np

df = df.fillna('')
np.savetxt(r'D:\Zishan\Programming\Python\Excel Data Cleaning Automation\np.txt', df.values, fmt='%s', delimiter=';')
