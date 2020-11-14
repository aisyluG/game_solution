import numpy as np
import pandas as pd

def vald(matrix: np.ndarray, strategys, states):
    report = '<h4>Исходные данные:</h4>'
    report += pd.DataFrame(data=matrix, columns=states, index=strategys).to_html()
    n, _ = matrix.shape
    mins = [min(matrix[x]) for x in range(n)]
    report += '<h4>Вычисление:</h4>'
    report += '<p>Минимумы:</p>'
    report += pd.DataFrame(data=mins, columns=['min Wij'], index=strategys).to_html()
    report += '<h4>Ответ:</h4>'
    report += f'<b>P = maxmin Wij = {max(mins)}</b><p> При данных условиях рациональным решением будет стратегия &laquo;{strategys[mins.index(max(mins))]}&raquo;</p>'
    return report

def bayes(matrix: np.ndarray, strategys, states, probabilities):
    report = '<h4>Исходные данные:</h4>'
    report += pd.DataFrame(data=matrix, columns=states, index=strategys).to_html()
    x = pd.DataFrame(data=probabilities, index=states, columns=['Вероятность']).transpose()
    report += x.to_html()
    n, _ = matrix.shape
    sums = [np.multiply(matrix[x], np.array(probabilities)).sum() for x in range(n)]
    report += '<h4>Вычисление:</h4>'
    report += pd.DataFrame(data=sums, columns=['&sum;WijPj'], index=strategys).to_html(escape=False)
    report += '<h4>Ответ:</h4>'
    report += f'<b>P = max&sum;WijPj = {max(sums)}</b><p> При данных условиях рациональным решением будет стратегия &laquo;{strategys[sums.index(max(sums))]}&raquo; </p>'
    return report

def savidge(matrix: np.ndarray, strategys, states):
    report = '<h4>Исходные данные:</h4>'
    report += pd.DataFrame(data=matrix, columns=states, index=strategys).to_html()
    report += '<h4>Вычисление:</h4>'
    n, m = matrix.shape
    Wj = [max(matrix[:, x]) for x in range(m)]
    report += pd.DataFrame(data=Wj, index=states, columns=['Wj']).transpose().to_html()
    matrix = [abs(matrix[:,x] - Wj[x]) for x in range(m)]
    report += '<p>Матрица рисков:</p>'
    report += pd.DataFrame(data=matrix, index=states, columns=strategys).transpose().to_html()
    maxs = [max(matrix[x]) for x in range(n)]
    report += pd.DataFrame(data=maxs, index=strategys, columns=['max(Wj-w)']).to_html()
    report += '<h4>Ответ:</h4>'
    report += f'<b>P = minmax(Wj - w) = {min(maxs)}</b><p> При данных условиях рациональным решением будет стратегия ' \
              f'&laquo;{strategys[maxs.index(min(maxs))]}&raquo; </p>'
    return report

def gurvits(matrix: np.ndarray, strategys, states, weight):
    report = '<h4>Исходные данные:</h4>'
    report += pd.DataFrame(data=matrix, columns=states, index=strategys).to_html()
    report += f'<p>Коэффициент пессимизма равен {weight}</p>'
    report += '<h4>Вычисление:</h4>'
    n, m = matrix.shape
    mins = [min(matrix[x]) for x in range(n)]
    maxs = [max(matrix[x]) for x in range(n)]
    report += pd.DataFrame(data=[mins, maxs], index=['min Wij', 'max Wij'], columns=strategys).transpose().to_html()
    p = weight*np.array(mins) + (1-weight)*np.array(maxs)
    report += pd.DataFrame(data=p, index=strategys, columns=['P']).to_html()
    report += '<h4>Ответ:</h4>'
    report += f'<b>P = max[&rho;minWij + (1 - &rho;)maxWij] = {p.max()}</b><p> При данных условиях рациональным решением будет стратегия ' \
              f'&laquo;{strategys[list(p).index(max(p))]}&raquo; </p>'
    return report

