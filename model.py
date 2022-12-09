import pickle
import pandas as pd
# global variable
global model, feature, data

def load():
    global model, feature, data
    model = pickle.load(open('model/model_ds.pkl', 'rb'))
    feature = pickle.load(open('model/list_feature.pkl', 'rb'))
    data = pd.read_pickle('model/database.pkl')

def recommendations(jenis_lembaga, provinsi, jenis_kelamin, umur, jenis_kekerasan):
  provinsi = provinsi.replace(" ","")
  umur = umur.replace(" ","")
  input = (jenis_lembaga)+' '+(provinsi)+' '+(umur)+' '+(jenis_kelamin)+' '+(jenis_kekerasan)
  input = input.lower()
  for index in range(len(feature)):
    if feature[index]==input:
      break

  nama_lembaga= data.iloc[index,0]
  jenis_lembaga= data.iloc[index,1]
  profile_lembaga= data.iloc[index,2]
  provinsi= data.iloc[index,3]
  alamat= data.iloc[index,4]
  kontak= data.iloc[index,5]
  jenis_kelamin= data.iloc[index,6]
  umur= data.iloc[index,7]
  jenis_kekerasan= data.iloc[index,8]
  
  return index, nama_lembaga, jenis_lembaga, profile_lembaga, provinsi, alamat, kontak, jenis_kelamin, umur, jenis_kekerasan

def recommendations_lembaga(index,number_of_recommendations=1): 
  similarity_scores = list(enumerate(model[index]))
  similarity_scores_sorted = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
  recommendations_indices = [t[0] for t in similarity_scores_sorted[1:(number_of_recommendations+1)]]

  rekom_nama=data['nama'].iloc[recommendations_indices]
  rekom_profile=data['profile'].iloc[recommendations_indices]
  rekom_alamat=data['alamat'].iloc[recommendations_indices]
  rekom_kontak=data['kontak'].iloc[recommendations_indices]

  return rekom_nama, rekom_profile, rekom_alamat, rekom_kontak