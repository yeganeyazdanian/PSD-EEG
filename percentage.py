import Data

data = Data.Fin_Means()

fp1_alpha = (data["Timed"]["percents"]["fp1"]["alpha"] / data["UnTimed"]["percents"]["fp1"]["alpha"]) * 100
fp1_beta = (data["Timed"]["percents"]["fp1"]["beta"] / data["UnTimed"]["percents"]["fp1"]["beta"]) * 100
fp1_theta = (data["Timed"]["percents"]["fp1"]["theta"] / data["UnTimed"]["percents"]["fp1"]["theta"]) * 100
fp2_alpha = (data["Timed"]["percents"]["fp2"]["alpha"] / data["UnTimed"]["percents"]["fp2"]["alpha"]) * 100
fp2_beta = (data["Timed"]["percents"]["fp2"]["beta"] / data["UnTimed"]["percents"]["fp2"]["beta"]) * 100
fp2_theta = (data["Timed"]["percents"]["fp2"]["theta"] / data["UnTimed"]["percents"]["fp2"]["theta"]) * 100
fpz_alpha = (data["Timed"]["percents"]["fpz"]["alpha"] / data["UnTimed"]["percents"]["fpz"]["alpha"]) * 100
fpz_beta = (data["Timed"]["percents"]["fpz"]["beta"] / data["UnTimed"]["percents"]["fpz"]["beta"]) * 100
fpz_theta = (data["Timed"]["percents"]["fpz"]["theta"] / data["UnTimed"]["percents"]["fpz"]["theta"]) * 100

output = """
        fp1        fp2        fpz
a       {:0.0f}%        {:0.0f}%        {:0.0f}%

b       {:0.0f}%        {:0.0f}%        {:0.0f}%

t       {:0.0f}%        {:0.0f}%        {:0.0f}%
""".format(fp1_alpha,fp2_alpha,fpz_alpha,fp1_beta,fp2_beta,fpz_beta,fp1_theta,fp2_theta,fpz_theta)

f = open('output.txt','w')
f.write(output)
f.close()
print(output)
