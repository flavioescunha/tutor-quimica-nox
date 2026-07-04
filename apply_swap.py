import re

with open('material_nox.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Swap the text "Verificação de Leitura 3" and "Verificação de Leitura 4"
content = content.replace('Verificação de Leitura 3', 'Verificação de Leitura TEMP')
content = content.replace('Verificação de Leitura 4', 'Verificação de Leitura 3')
content = content.replace('Verificação de Leitura TEMP', 'Verificação de Leitura 4')

# Wait, this text swap is just visual. 
# But the IDs in HTML and JS need to be swapped to match the reading order.
# quiz-4 (Pauling definition) should be quiz-3
# quiz-3 (Electronegativity comparison) should be quiz-4

content = content.replace('quiz-3', 'quiz-temp')
content = content.replace('quiz-4', 'quiz-3')
content = content.replace('quiz-temp', 'quiz-4')

content = content.replace('Quiz3', 'QuizTemp')
content = content.replace('Quiz4', 'Quiz3')
content = content.replace('QuizTemp', 'Quiz4')

content = content.replace('currentQuiz3', 'currentQuizTemp')
# wait, there is no currentQuiz4 in the script. I'll just change currentQuiz3 to currentQuiz4.
content = content.replace('currentQuizTemp', 'currentQuiz4')


# Now modify the new Quiz 3 (which was Quiz 4) to shuffle options and remove A, B, C, D
# Looking for the quiz-3-details block (which contains the options)
# We will replace the static options with an empty div and generate them in generateQuiz3()

# Find the quiz-options block in the new quiz-3
old_options = r"""<div class="quiz-options" style="display: flex; flex-direction: column; gap: 0.5rem; margin: 1rem 0;">
                    <label style="padding: 0.5rem; background: var(--bg-tertiary); border: 1px solid var(--border); border-radius: var(--radius-sm); cursor: pointer;">
                        <input type="radio" name="quiz-3-radio" value="A"> A\) Calculando a massa de cada átomo e dividindo pelo número de elétrons\.
                    </label>
                    <label style="padding: 0.5rem; background: var(--bg-tertiary); border: 1px solid var(--border); border-radius: var(--radius-sm); cursor: pointer;">
                        <input type="radio" name="quiz-3-radio" value="B"> B\) Medindo a temperatura de fusão de cada elemento isolado na natureza\.
                    </label>
                    <label style="padding: 0.5rem; background: var(--bg-tertiary); border: 1px solid var(--border); border-radius: var(--radius-sm); cursor: pointer;">
                        <input type="radio" name="quiz-3-radio" value="C"> C\) Comparando a energia necessária para quebrar ligações químicas e atribuindo o valor máximo 4,0 ao Flúor\.
                    </label>
                    <label style="padding: 0.5rem; background: var(--bg-tertiary); border: 1px solid var(--border); border-radius: var(--radius-sm); cursor: pointer;">
                        <input type="radio" name="quiz-3-radio" value="D"> D\) Através da contagem direta do número de nêutrons no núcleo dos átomos metálicos\.
                    </label>
                </div>"""

new_options = """<div id="quiz-3-options" class="quiz-options" style="display: flex; flex-direction: column; gap: 0.5rem; margin: 1rem 0;">
                    <!-- Opções geradas via JS -->
                </div>"""

content = re.sub(old_options, new_options, content)

# Also, the previous Quiz 4 (now Quiz 3) didn't have a generate function. It just had checkQuiz4.
# Let's add generateQuiz3 to it, and rename checkQuiz3.

# Look for checkQuiz3 logic (which is the Pauling quiz)
# And replace it with generateQuiz3 and checkQuiz3.
old_logic = r"""// ===== LÓGICA DO QUIZ 3 =====
    function checkQuiz3\(\) \{
        const radios = document\.getElementsByName\('quiz-3-radio'\);
        let selected = null;
        for \(let r of radios\) \{
            if \(r\.checked\) \{
                selected = r\.value;
                break;
            \}
        \}
        
        const feedback = document\.getElementById\('quiz-3-feedback'\);
        const status = document\.getElementById\('quiz-3-status'\);
        
        if \(!selected\) \{
            feedback\.innerHTML = 'Por favor, selecione uma das alternativas\.';
            feedback\.className = 'feedback-msg error';
            return;
        \}
        
        if \(selected === 'C'\) \{
            feedback\.innerHTML = '🎉 Correto! Pauling usou a energia de quebra das ligações químicas e atribuiu 4,0 ao Flúor como referência máxima\.';
            feedback\.className = 'feedback-msg success';
            status\.className = 'quiz-status correct';
            status\.innerHTML = 'Correto';
            
            setTimeout\(\(\) => \{
                document\.getElementById\('quiz-3-details'\)\.open = false;
            \}, 3000\);
        \} else \{
            feedback\.innerHTML = '❌ Incorreto\. Releia o quadro sobre como Pauling definiu esses valores relativos \(não têm relação direta com massa, temperatura de fusão ou nêutrons\)\.';
            feedback\.className = 'feedback-msg error';
            status\.className = 'quiz-status wrong';
            status\.innerHTML = 'Incorreto';
        \}
    \}"""

new_logic = """// ===== LÓGICA DO QUIZ 3 (Pauling) =====
    function generateQuiz3() {
        const options = [
            { id: 'wrong1', text: 'Calculando a massa de cada átomo e dividindo pelo número de elétrons.' },
            { id: 'wrong2', text: 'Medindo a temperatura de fusão de cada elemento isolado na natureza.' },
            { id: 'correct', text: 'Comparando a energia necessária para quebrar ligações químicas e atribuindo o valor máximo 4,0 ao Flúor.' },
            { id: 'wrong3', text: 'Através da contagem direta do número de nêutrons no núcleo dos átomos metálicos.' }
        ];
        
        // Shuffle options
        options.sort(() => Math.random() - 0.5);
        
        const container = document.getElementById('quiz-3-options');
        container.innerHTML = '';
        
        options.forEach(opt => {
            container.innerHTML += `
                <label style="padding: 0.5rem; background: var(--bg-tertiary); border: 1px solid var(--border); border-radius: var(--radius-sm); cursor: pointer;">
                    <input type="radio" name="quiz-3-radio" value="${opt.id}"> ${opt.text}
                </label>
            `;
        });
        
        document.getElementById('quiz-3-feedback').className = 'feedback-msg';
        document.getElementById('quiz-3-feedback').innerHTML = '';
        const status = document.getElementById('quiz-3-status');
        status.className = 'quiz-status pending';
        status.innerHTML = 'Pendente';
    }

    function checkQuiz3() {
        const radios = document.getElementsByName('quiz-3-radio');
        let selected = null;
        for (let r of radios) {
            if (r.checked) {
                selected = r.value;
                break;
            }
        }
        
        const feedback = document.getElementById('quiz-3-feedback');
        const status = document.getElementById('quiz-3-status');
        
        if (!selected) {
            feedback.innerHTML = 'Por favor, selecione uma das alternativas.';
            feedback.className = 'feedback-msg error';
            return;
        }
        
        if (selected === 'correct') {
            feedback.innerHTML = '🎉 Correto! Pauling usou a energia de quebra das ligações químicas e atribuiu 4,0 ao Flúor como referência máxima.';
            feedback.className = 'feedback-msg success';
            status.className = 'quiz-status correct';
            status.innerHTML = 'Correto';
            
            setTimeout(() => {
                document.getElementById('quiz-3-details').open = false;
            }, 3000);
        } else {
            feedback.innerHTML = '❌ Incorreto. Releia o quadro sobre como Pauling definiu esses valores relativos (não têm relação direta com massa, temperatura de fusão ou nêutrons).';
            feedback.className = 'feedback-msg error';
            status.className = 'quiz-status wrong';
            status.innerHTML = 'Incorreto';
        }
    }"""
    
content = re.sub(old_logic, new_logic, content)

# I need to ensure generateQuiz3() is called on page load. It was called before when it was quiz4, wait no, Quiz 4 didn't have generateQuiz4().
# Let's find DOMContentLoaded:
# window.addEventListener('DOMContentLoaded', () => {
#        generateQuiz1();
#        generateQuiz2();
#        generateQuiz4(); // wait, earlier I appended generateQuiz3() for the electronegativity one. Now that one is generateQuiz4().
#    });

content = content.replace("generateQuiz3();", "generateQuiz3();\n        generateQuiz4();")


with open('material_nox.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Quiz swap and logic updated.")
