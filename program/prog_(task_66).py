def count_smileys(arr):
    count = 0
    lis = [':)',':-)',':~)',';)',';-)',';~)',':D',':-D',':~D',';D',';-D',';~D']
    for x in arr:
        if x in lis:
            count +=1
    return count



print(count_smileys([';]', ':[', ';*', ':$', ';-D']))