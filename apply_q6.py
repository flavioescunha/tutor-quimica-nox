import re

with open('material_nox.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Quiz 5 modification
old_q5_js = r"// ===== LÓGICA DO QUIZ 5 =====(.+?)(?=</script>)"

def get_q5_q6_js():
    return """// ===== LÓGICA DO QUIZ 5 =====
    let currentQuiz5 = null;
    
    function generateQuiz5() {
        const compounds = [
            { formula: 'NaCl', el1: 'Na', el2: 'Cl', nox1: '+1', nox2: '-1', g1: 'Metais Alcalinos', g2: 'Halogênios' },
            { formula: 'KCl', el1: 'K', el2: 'Cl', nox1: '+1', nox2: '-1', g1: 'Metais Alcalinos', g2: 'Halogênios' },
            { formula: 'MgCl₂', el1: 'Mg', el2: 'Cl', nox1: '+2', nox2: '-1', g1: 'Alcalinoterrosos', g2: 'Halogênios' },
            { formula: 'CaCl₂', el1: 'Ca', el2: 'Cl', nox1: '+2', nox2: '-1', g1: 'Alcalinoterrosos', g2: 'Halogênios' },
            { formula: 'Na₂O', el1: 'Na', el2: 'O', nox1: '+1', nox2: '-2', g1: 'Metais Alcalinos', g2: 'Outros Ametais' },
            { formula: 'K₂O', el1: 'K', el2: 'O', nox1: '+1', nox2: '-2', g1: 'Metais Alcalinos', g2: 'Outros Ametais' },
            { formula: 'MgO', el1: 'Mg', el2: 'O', nox1: '+2', nox2: '-2', g1: 'Alcalinoterrosos', g2: 'Outros Ametais' },
            { formula: 'CaO', el1: 'Ca', el2: 'O', nox1: '+2', nox2: '-2', g1: 'Alcalinoterrosos', g2: 'Outros Ametais' },
            { formula: 'AlCl₃', el1: 'Al', el2: 'Cl', nox1: '+3', nox2: '-1', g1: 'Metais Pós-Transição', g2: 'Halogênios' },
            { formula: 'Al₂O₃', el1: 'Al', el2: 'O', nox1: '+3', nox2: '-2', g1: 'Metais Pós-Transição', g2: 'Outros Ametais' }
        ];
        
        if (!window.usedQuiz5) window.usedQuiz5 = [];
        let available = compounds.filter(c => !window.usedQuiz5.includes(c.formula));
        if (available.length === 0) {
            window.usedQuiz5 = [];
            available = compounds;
        }
        currentQuiz5 = available[Math.floor(Math.random() * available.length)];
        window.usedQuiz5.push(currentQuiz5.formula);
        
        document.getElementById('quiz-5-compound').innerHTML = currentQuiz5.formula;
        
        const groupOptions = `
            <option value="">Selecione...</option>
            <option value="Hidrogênio">Hidrogênio</option>
            <option value="Metais Alcalinos">Metais Alcalinos</option>
            <option value="Alcalinoterrosos">Alcalinoterrosos</option>
            <option value="Metais de Transição">Metais de Transição</option>
            <option value="Metais Pós-Transição">Metais Pós-Transição</option>
            <option value="Semimetais">Semimetais</option>
            <option value="Outros Ametais">Outros Ametais</option>
            <option value="Halogênios">Halogênios</option>
            <option value="Gases Nobres">Gases Nobres</option>
        `;
        
        document.getElementById('quiz-5-inputs').innerHTML = `
            <div style="display: flex; flex-direction: column; gap: 0.5rem; background: var(--bg-secondary); padding: 1rem; border-radius: 8px;">
                <div style="font-weight: bold; margin-bottom: 0.5rem; text-align: center;">Elemento: ${currentQuiz5.el1}</div>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    Família: 
                    <select id="quiz-5-g1" style="margin-left: 0.5rem; width: 150px; padding: 0.2rem;">${groupOptions}</select>
                </label>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    NOX: 
                    <input type="text" id="quiz-5-nox1" placeholder="Ex: +1" style="margin-left: 0.5rem; width: 150px;">
                </label>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 0.5rem; background: var(--bg-secondary); padding: 1rem; border-radius: 8px;">
                <div style="font-weight: bold; margin-bottom: 0.5rem; text-align: center;">Elemento: ${currentQuiz5.el2}</div>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    Família: 
                    <select id="quiz-5-g2" style="margin-left: 0.5rem; width: 150px; padding: 0.2rem;">${groupOptions}</select>
                </label>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    NOX: 
                    <input type="text" id="quiz-5-nox2" placeholder="Ex: -2" style="margin-left: 0.5rem; width: 150px;">
                </label>
            </div>
        `;
        
        document.getElementById('quiz-5-feedback').className = 'feedback-msg';
        document.getElementById('quiz-5-feedback').innerHTML = '';
        const status = document.getElementById('quiz-5-status');
        status.className = 'quiz-status pending';
        status.innerHTML = 'Pendente';
        document.getElementById('quiz-5-details').open = true;
    }

    function checkQuiz5() {
        const nox1 = document.getElementById('quiz-5-nox1').value.trim().replace(' ', '');
        const nox2 = document.getElementById('quiz-5-nox2').value.trim().replace(' ', '');
        const g1 = document.getElementById('quiz-5-g1').value;
        const g2 = document.getElementById('quiz-5-g2').value;
        
        const feedback = document.getElementById('quiz-5-feedback');
        const status = document.getElementById('quiz-5-status');
        
        if (!nox1 || !nox2 || !g1 || !g2) {
            feedback.innerHTML = 'Por favor, preencha o NOX e a Família de ambos os elementos.';
            feedback.className = 'feedback-msg error';
            return;
        }
        
        if (nox1 === currentQuiz5.nox1 && nox2 === currentQuiz5.nox2 && g1 === currentQuiz5.g1 && g2 === currentQuiz5.g2) {
            feedback.innerHTML = `🎉 Correto! O ${currentQuiz5.el1} é dos ${currentQuiz5.g1} (NOX ${currentQuiz5.nox1}) e o ${currentQuiz5.el2} é dos ${currentQuiz5.g2} (NOX ${currentQuiz5.nox2}).`;
            feedback.className = 'feedback-msg success';
            status.className = 'quiz-status correct';
            status.innerHTML = 'Correto';
            
            setTimeout(() => {
                document.getElementById('quiz-5-details').open = false;
            }, 3000);
        } else {
            feedback.innerHTML = `❌ Incorreto. Revise a família de cada elemento na tabela acima e lembre-se: Metais tendem a perder (NOX +), Ametais a ganhar (NOX -).`;
            feedback.className = 'feedback-msg error';
            status.className = 'quiz-status wrong';
            status.innerHTML = 'Incorreto';
        }
    }

    // ===== LÓGICA DO QUIZ 6 =====
    let currentQuiz6 = null;
    
    function generateQuiz6() {
        const compounds = [
            { formula: 'H₂O', el1: 'H', el2: 'O', nox1: '+1', nox2: '-2', g1: 'Hidrogênio', g2: 'Outros Ametais' },
            { formula: 'CO₂', el1: 'C', el2: 'O', nox1: '+4', nox2: '-2', g1: 'Outros Ametais', g2: 'Outros Ametais' },
            { formula: 'CH₄', el1: 'C', el2: 'H', nox1: '-4', nox2: '+1', g1: 'Outros Ametais', g2: 'Hidrogênio' },
            { formula: 'NH₃', el1: 'N', el2: 'H', nox1: '-3', nox2: '+1', g1: 'Outros Ametais', g2: 'Hidrogênio' },
            { formula: 'SO₂', el1: 'S', el2: 'O', nox1: '+4', nox2: '-2', g1: 'Outros Ametais', g2: 'Outros Ametais' },
            { formula: 'PCl₃', el1: 'P', el2: 'Cl', nox1: '+3', nox2: '-1', g1: 'Outros Ametais', g2: 'Halogênios' },
            { formula: 'N₂O', el1: 'N', el2: 'O', nox1: '+1', nox2: '-2', g1: 'Outros Ametais', g2: 'Outros Ametais' },
            { formula: 'OF₂', el1: 'O', el2: 'F', nox1: '+2', nox2: '-1', g1: 'Outros Ametais', g2: 'Halogênios' },
            { formula: 'CCl₄', el1: 'C', el2: 'Cl', nox1: '+4', nox2: '-1', g1: 'Outros Ametais', g2: 'Halogênios' },
            { formula: 'HCl', el1: 'H', el2: 'Cl', nox1: '+1', nox2: '-1', g1: 'Hidrogênio', g2: 'Halogênios' }
        ];
        
        if (!window.usedQuiz6) window.usedQuiz6 = [];
        let available = compounds.filter(c => !window.usedQuiz6.includes(c.formula));
        if (available.length === 0) {
            window.usedQuiz6 = [];
            available = compounds;
        }
        currentQuiz6 = available[Math.floor(Math.random() * available.length)];
        window.usedQuiz6.push(currentQuiz6.formula);
        
        document.getElementById('quiz-6-compound').innerHTML = currentQuiz6.formula;
        
        const groupOptions = `
            <option value="">Selecione...</option>
            <option value="Hidrogênio">Hidrogênio</option>
            <option value="Metais Alcalinos">Metais Alcalinos</option>
            <option value="Alcalinoterrosos">Alcalinoterrosos</option>
            <option value="Metais de Transição">Metais de Transição</option>
            <option value="Metais Pós-Transição">Metais Pós-Transição</option>
            <option value="Semimetais">Semimetais</option>
            <option value="Outros Ametais">Outros Ametais</option>
            <option value="Halogênios">Halogênios</option>
            <option value="Gases Nobres">Gases Nobres</option>
        `;
        
        document.getElementById('quiz-6-inputs').innerHTML = `
            <div style="display: flex; flex-direction: column; gap: 0.5rem; background: var(--bg-secondary); padding: 1rem; border-radius: 8px;">
                <div style="font-weight: bold; margin-bottom: 0.5rem; text-align: center;">Elemento: ${currentQuiz6.el1}</div>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    Família: 
                    <select id="quiz-6-g1" style="margin-left: 0.5rem; width: 150px; padding: 0.2rem;">${groupOptions}</select>
                </label>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    NOX: 
                    <input type="text" id="quiz-6-nox1" placeholder="Ex: +1" style="margin-left: 0.5rem; width: 150px;">
                </label>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 0.5rem; background: var(--bg-secondary); padding: 1rem; border-radius: 8px;">
                <div style="font-weight: bold; margin-bottom: 0.5rem; text-align: center;">Elemento: ${currentQuiz6.el2}</div>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    Família: 
                    <select id="quiz-6-g2" style="margin-left: 0.5rem; width: 150px; padding: 0.2rem;">${groupOptions}</select>
                </label>
                <label style="font-size: 1rem; display: flex; justify-content: space-between; align-items: center;">
                    NOX: 
                    <input type="text" id="quiz-6-nox2" placeholder="Ex: -2" style="margin-left: 0.5rem; width: 150px;">
                </label>
            </div>
        `;
        
        document.getElementById('quiz-6-feedback').className = 'feedback-msg';
        document.getElementById('quiz-6-feedback').innerHTML = '';
        const status = document.getElementById('quiz-6-status');
        status.className = 'quiz-status pending';
        status.innerHTML = 'Pendente';
        document.getElementById('quiz-6-details').open = true;
    }

    function checkQuiz6() {
        const nox1 = document.getElementById('quiz-6-nox1').value.trim().replace(' ', '');
        const nox2 = document.getElementById('quiz-6-nox2').value.trim().replace(' ', '');
        const g1 = document.getElementById('quiz-6-g1').value;
        const g2 = document.getElementById('quiz-6-g2').value;
        
        const feedback = document.getElementById('quiz-6-feedback');
        const status = document.getElementById('quiz-6-status');
        
        if (!nox1 || !nox2 || !g1 || !g2) {
            feedback.innerHTML = 'Por favor, preencha o NOX e a Família de ambos os elementos.';
            feedback.className = 'feedback-msg error';
            return;
        }
        
        if (nox1 === currentQuiz6.nox1 && nox2 === currentQuiz6.nox2 && g1 === currentQuiz6.g1 && g2 === currentQuiz6.g2) {
            feedback.innerHTML = `🎉 Correto! O ${currentQuiz6.el1} tem NOX ${currentQuiz6.nox1} e o ${currentQuiz6.el2} tem NOX ${currentQuiz6.nox2}. Nas ligações covalentes, o elemento mais eletronegativo fica com a carga (NOX) aparente negativa.`;
            feedback.className = 'feedback-msg success';
            status.className = 'quiz-status correct';
            status.innerHTML = 'Correto';
            
            setTimeout(() => {
                document.getElementById('quiz-6-details').open = false;
            }, 3000);
        } else {
            feedback.innerHTML = `❌ Incorreto. Lembre-se: em compostos covalentes, o elemento mais eletronegativo puxa os elétrons e fica com NOX negativo. Revise a tabela de eletronegatividade!`;
            feedback.className = 'feedback-msg error';
            status.className = 'quiz-status wrong';
            status.innerHTML = 'Incorreto';
        }
    }
"""

match = re.search(old_q5_js, content, flags=re.DOTALL)
if match:
    content = content.replace(match.group(0), get_q5_q6_js())

quiz_6_html = """
        <details class="quiz-box" id="quiz-6-details" style="margin-bottom: 2rem;">
            <summary class="quiz-summary">
                <h4>📝 Verificação de Leitura 6</h4>
                <span class="quiz-status pending" id="quiz-6-status">Pendente</span>
            </summary>
            <div class="quiz-content">
                <p>Com base no que você aprendeu sobre compostos moleculares (covalentes) e eletronegatividade, determine o NOX de cada elemento no composto abaixo (Lembrete: o mais eletronegativo fica negativo!):</p>
                <div class="equation" id="quiz-6-compound" style="font-size: 2rem; font-weight: bold; color: var(--text-primary); margin: 1.5rem 0;">
                    <!-- Gerado via JS -->
                </div>
                <div class="quiz-inputs-inline" style="justify-content: center; gap: 1.5rem; margin-bottom: 1.5rem;" id="quiz-6-inputs">
                    <!-- Gerado via JS -->
                </div>
                <div style="text-align: center;">
                    <button onclick="checkQuiz6()" class="btn-quiz">Verificar Resposta</button>
                    <button onclick="generateQuiz6()" class="btn-quiz" style="background: var(--bg-tertiary); margin-left: 0.5rem;">Gerar Outro Composto</button>
                </div>
                <div id="quiz-6-feedback" class="feedback-msg"></div>
            </div>
        </details>
"""

# Insert quiz 6 HTML after the covalent compound equations section.
target_q6 = """                N ≡ N   Como os átomos são iguais, a diferença é zero.<br>
            <small style="color: var(--text-muted);">NOX de cada N = 0</small>
        </div>"""

if target_q6 in content:
    content = content.replace(target_q6, target_q6 + "\n\n" + quiz_6_html)
else:
    print("Could not find insert point for quiz 6 html")

# Ensure DOMContentLoaded calls generateQuiz6
content = content.replace("generateQuiz5();\n    });", "generateQuiz5();\n        generateQuiz6();\n    });")

with open('material_nox.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Quiz 5 modified and Quiz 6 added")
