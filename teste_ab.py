import numpy as np
from scipy.stats import ttest_ind

# dados do grupo de controle
control_group = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

# dados do grupo de teste
test_group = np.array([0.2, 0.3, 0.4, 0.5, 0.6])

# calcular a média e o desvio padrão para cada grupo
control_mean = np.mean(control_group)
test_mean = np.mean(test_group)
control_std = np.std(control_group)
test_std = np.std(test_group)

# executar o teste t de duas amostras usando a função ttest_ind
t_stat, p_value = ttest_ind(test_group, control_group, equal_var=False)

# imprimir os resultados
print('Controle - média: {:.3f}, desvio padrão: {:.3f}'.format(control_mean, control_std))
print('Teste - média: {:.3f}, desvio padrão: {:.3f}'.format(test_mean, test_std))
print('Teste t: {:.3f}, p-value: {:.3f}'.format(t_stat, p_value))
