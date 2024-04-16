#include <iostream>
#include <fstream>
#include <cmath>
#include <complex>
#include <cstring>
#include <cstdlib>
using namespace std;

double calcz(complex<double> z, complex<double> c, double zabsmax) {
    int nit = 0;
    int nitmax = 1000;
    double ratio = 0.0;
    while (abs(z) < zabsmax && nit < nitmax) {
        z = pow(z,2) + c;
        nit += 1;
        ratio = (double(nit) / nitmax) * 255.0;
    }
    return ratio;
}

void julia_loop(double ***julia, long im_width, long im_height, double xwidth, double yheight, double xmin, double ymin, long nitmax) {
    double zabsmax = 10.0;
    complex<double> c(-0.1,0.65);
    (*julia) = new double*[im_width];
    for (long i = 0; i < im_width; i++) {
        (*julia)[i] = new double[im_height];
        for (long j = 0; j < im_height; j++) {
            int nit = 0;
            complex<double> z(double(i) / im_width * xwidth + xmin,
            double(j) / im_height * yheight + ymin);
            (*julia)[i][j] = calcz(z,c,zabsmax);
        }
    }
}

int main(int argc, char **argv) {
    char *file;
    if (argc > 1) {
        file = argv[1];
    }
    else {
        file = "juliadata.txt";
    }
    cout << "Julia set fractal generator\n" << endl;
    long im_width = 1000;
    long im_height = 1000;
    double xmin = -0.5, xmax = 0.5;
    double xwidth = xmax - xmin;
    double ymin = -0.5, ymax = 0.5;
    double yheight = ymax - ymin;
    long nitmax = 1000;
    double **julia;
    julia_loop(&julia, im_width, im_height, xwidth, yheight, xmin, ymin, nitmax);
    ofstream outfile(file);
    outfile << im_width << endl;
    outfile << im_height << endl;
    outfile << xmin << endl;
    outfile << xmax << endl;
    outfile << xwidth << endl;
    outfile << ymin << endl;
    outfile << ymax << endl;
    outfile << yheight << endl;
    for (long i = 0; i < im_width; i++) {
        for (long j = 0; j < im_height; j++) {
            outfile << julia[i][j] << "\t";
        }
    }
    outfile << endl;
    outfile.close();
    for (long i = 0; i < im_width; i++) {
        delete[] julia[i];
    }
    delete[] julia;
    return 0;
}
