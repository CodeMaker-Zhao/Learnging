import matplotlib.pyplot as plt

input_value = [value for value in range(1,1001)]
squares = [value**3 for value  in input_value]

plt.scatter(input_value,squares,cmap=plt.cm.Blues,c=squares,s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Sauqre of Value', fontsize=14)

plt.tick_params(axis='both', which = 'major', labelsize = 14)

plt.show()