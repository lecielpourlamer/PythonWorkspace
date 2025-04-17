import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# {'이름': '스누피', '나이': 30, '취미': ['축구', '골프', '코딩']}
