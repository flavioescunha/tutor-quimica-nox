import re
import random

with open('material_nox.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Swap the names in the HTML and JS:
# What was quiz-4 becomes quiz-3 (reading order 3)
# What was quiz-3 becomes quiz-4 (reading order 4)

# To avoid conflicts, we swap them by using temporary names
content = content.replace('quiz-3', 'quiz-temp')
content = content.replace('quiz-4', 'quiz-3')
content = content.replace('quiz-temp', 'quiz-4')

content = content.replace('Quiz 3', 'Quiz Temp')
content = content.replace('Quiz 4', 'Quiz 3')
content = content.replace('Quiz Temp', 'Quiz 4')

content = content.replace('Verificação de Leitura 3', 'Verificação de Leitura Temp')
content = content.replace('Verificação de Leitura 4', 'Verificação de Leitura 3')
content = content.replace('Verificação de Leitura Temp', 'Verificação de Leitura 4')

# Wait, `currentQuiz3` was in JS, now it's `currentQuiz4`.
content = content.replace('currentQuiz3', 'currentQuiz4')
content = content.replace('currentQuiz4', 'currentQuiz3') # Wait, I didn't have currentQuiz4!
# Let's fix that. Since I just replaced quiz-3 with quiz-temp, let's do JS variables manually.

# It's actually safer to just do regex replacement for the IDs and function names.
pass
