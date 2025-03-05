# Diffusion-7.2
## Описание задачи
К картине случайных блужданий из `dif_7_1` добавить гистограмму распределения частиц по координатам. Предусмотреть в программе возможность перестроек гистограммы при изменении числа бинов. Гистограмма должна динамически перестраиваться с увеличением числа шагов. \
Теоретические предсказания утверждают, что координаты частиц будут подчиняться **распределению Гаусса**. На каждом шаге вычислите “экспериментальные” параметры распределения Гаусса и выведите функцию распределения на тот же график, что и гистограмма. \
Сравните среднеквадратичное отклонение, полученное по вашему набору блуждающих частиц с теоретическим предсказанием. При каком количестве шагов отличия между экспериментальным и теоретическим значением будет меньше `1%`. Зависит ли это количество шагов от числа частиц, участвующих в моделировании?
