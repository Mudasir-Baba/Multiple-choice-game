end_result = 0
question = 'Where is Eifel tower located?(Write option name like "a")'
correct_answer = 'a'
ans = input(question + '\n(a.Paris)\n(b.London)\n(c.Hong Kong)\n>>>').lower()

if ans == correct_answer:
    end_result += 1
    print('Correct answer!')
elif ans != correct_answer:
    print(f'Ops wrong answer, the correct answer is {correct_answer}')


question = '\nWhere are the pyramids located'
correct_answer = 'c'
ans = input(question + '\n(a.Peru)\n(b.Jerusalem)\n(c.Giza)\n>>>').lower()
if ans == correct_answer:
    end_result += 1
    print('Correct answer!')
elif ans != correct_answer:
    print(f'Ops wrong answer!, the correct answer is {correct_answer}')


question = '\nWhere is the statue of liberty located'
correct_answer = 'c'
ans = input(question + '\n(a.Russai)\n(b.France)\n(c.USA)\n>>>').lower()
if ans == correct_answer:
    end_result += 1
    print('Correct answer')
elif ans != correct_answer:
    print(f'Ops wrong answer, the correct answer is {correct_answer}')


print(f'You got  {end_result} out of 3 answers correctly.')