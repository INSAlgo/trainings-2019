import matplotlib.pyplot as plt

# Geometric operations


def det(a, b):
    return a.real * b.imag - a.imag * b.real


def akward_det(p, q, r):
    a = det(p, q)
    b = det(p, r)
    c = det(q, r)
    return a - b + c


def point_left_line(p, q, r):
    '''
    return True iff r lies to the left of the segment [p, q]
    '''
    return akward_det(p, q, r) >= 0


def point_strictly_left_line(p, q, r):
    '''
    return True iff r lies to the left of the segment [p, q],
    and not on the line (p, q)
    '''
    return akward_det(p, q, r) > 0


def point_right_line(p, q, r):
    '''
    return True iff r lies to the right of the segment [p, q]
    '''
    return akward_det(p, q, r) <= 0


def point_strictly_right_line(p, q, r):
    '''
    return True iff r lies to the right of the segment [p, q],
    and not on the line (p, q)
    '''
    return akward_det(p, q, r) < 0


def point_on_line(p, q, r):
    '''
    return True iff r lies on the line (p, q),
    '''
    return akward_det(p, q, r) == 0


def quick_sort(L, order):
    def switch(i, j):
        temp = L[i]
        L[i] = L[j]
        L[j] = temp

    def aux(i, j):
        if i < j:
            pivot = r.randint(i, j - 1)
            switch(i, pivot)
            pivot = i
            k = i + 1
            while k < j:
                if order(L[k], L[pivot]):
                    switch(k, pivot + 1)
                    switch(pivot, pivot + 1)
                    pivot += 1
                k += 1
            aux(i, pivot)
            aux(pivot + 1, j)

    aux(0, len(L))


def point_left_point(a, b):
    if(a.real == b.real):
        return a.imag >= b.imag
    return a.real < b.real


def left_right_sort(L):
    '''
    L is a list of points,
    sorts L from left to right
    '''
    quick_sort(L, point_left_point)

# Displays


def plot_points(L, col='k'):
    '''
    plots all the points of L
    colors : 'k' black
             'r' red
             'b' blue
             'g' green
    '''
    X = [z.real for z in L]
    Y = [z.imag for z in L]

    plt.plot(X, Y, col + '.')


def plot_chain(L, col='k'):
    '''
    plots the segemnts [L[i], L[i+1]] for i=0 to len(L)-2
    colors : 'k' black
             'r' red
             'b' blue
             'g' green
    '''
    plot_points(L, col)

    for i in range(len(L) - 1):
        plt.plot([L[i].real, L[i + 1].real], [L[i].imag, L[i + 1].imag], col)


def plot_polygon(P, col='k'):
    '''
    plots the polygon P
    colors : 'k' black
             'r' red
             'b' blue
             'g' green
    '''
    plot_points(L, col)

    for i in range(len(L) - 1):
        plt.plot([L[i].real, L[i + 1].real], [L[i].imag, L[i + 1].imag], col)
    plt.plot([L[0].real, L[-1].real], [L[0].imag, L[-1].imag], col)


def show():
    plt.axis('equal')
    plt.show()

# The convex hulls
# Algorithms from the presentation


def Jarvis(L):
    CH = []
    # compute CH here

    plot_points(L)
    plot_polygon(CH, 'r')
    show()


def Usual_algo(L):
    CH = []
    left_right_sort(L)
    Upper_hull = []
    Lower_hull = []
    # compute the parts of the hull here
    # and update CH in consequence

    plot_points(L)
    plot_polygon(CH, 'r')
    show()

# Now some exercises


def Convex_hull_of_a_polygon(P):
    '''
    P is a polygon (!)
    make a O(n) algorithm that computes the convex hull of P
    '''
    CH = []
    # compute CH here

    plot_polygon(P)
    plot_polygon(CH, 'r')
    show()


def Divide_and_conqeer_convex_hull(L):
    '''
    L is a list of points
    make O(n ln(n)) algorithm that computes the convex hull of L
    with a divide and conqeer approach
    '''
    CH = []
    # compute CH here

    plot_points(L)
    plot_polygon(CH, 'r')
    show()
