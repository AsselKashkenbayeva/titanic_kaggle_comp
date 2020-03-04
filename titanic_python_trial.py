import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Upload_data:

	def __init__(self, input_path):
		self.train = pd.read_csv(abs_path + '/train.csv')
		self.test = pd.read_csv(abs_path + '/test.csv')
		print ('Download complete!')
		
abs_path = "/Users/assel2/python_dir/titanic_kaggle_comp"
data = Upload_data(abs_path)

train_df = pd.DataFrame(data.train)
test_df = pd.DataFrame(data.test)
print(test_df.head(3))

women = train_df.loc[train_df.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
print('% of women who survived:', rate_women)

men = train_df.loc[train_df.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)
print('% male who survived:', rate_men)

def compare_columns(input_df,col, dp_col):
 
    uniq_var = input_df[col].unique()
    print(uniq_var)
    uniq_var_2 = input_df[dp_col].unique()
    print(uniq_var_2)

    new_dict = {}
    for j in uniq_var_2:
        for i in uniq_var:
            input_df['new_col']= np.where((input_df[col] == i) & (input_df[dp_col] == j), True, False)
            #print(train_df['new_col'].value_counts())
            
            value_inp = input_df['new_col'].value_counts().tolist()
            key_inp = input_df['new_col'].value_counts().index.tolist()
            count_1 = 0
            for m in key_inp:
                name = str(i) + str(j) + str(m)
                new_dict[name] = value_inp[count_1]
                count_1 +=1
    return new_dict

print(list(train_df))
col_names = list(train_df)
class_number = compare_columns(train_df,'Pclass', 'Sex')
print(class_number)



'''
train_df['new_col']= np.where((train_df['Survived'] == 1) & (train_df['Pclass'] == 1), True, False)
print(train_df['new_col'])
 for i in uniq_var:
        uniq_var_count = input_df[input_df[col] == i].shape[0]
        new_dict[i] = uniq_var_count

'''