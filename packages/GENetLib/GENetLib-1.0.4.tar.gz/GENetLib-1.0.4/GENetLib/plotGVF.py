def plotGVF(x, y = None, xlab = None, ylab = None):
    
    from plotFD import plotFD
    
    gvf = x
    if y == None:
        plotFD(gvf, xlab, ylab)
    else:
        plotFD(gvf, y, xlab, ylab)

