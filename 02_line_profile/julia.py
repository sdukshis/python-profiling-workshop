"""Julia set generator """
import line_profiler

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c = -0.62772 -.42193j


@line_profiler.profile
def calculate_z_serial_purepython(maxiter, zs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        z = zs[i]
        for _ in range(maxiter):
            z = z * z + c
        if abs(z) < 2:
            output[i] = 1
    return output


@line_profiler.profile
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex co-ordinates (zs) and complex parameters (cs), build Julia set and display"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # set width and height to the generated pixel counts, rather than the
    # pre-rounding desired width and height
    # build a list of co-ordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our function
    zs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))

    return calculate_z_serial_purepython(max_iterations, zs)


def test_julia(benchmark):
    result = benchmark(calc_pure_python, desired_width=1000, max_iterations=300)