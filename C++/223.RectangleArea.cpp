/*
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
 */
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int res = (C-A) * (D-B) + (G-E) * (H-F);
        if(!(A >= G || B >= H || C <= E || D <= F)){
            res -= (min(C, G) - max(A, E)) * (min(D, H) - max(B, F));
        }
        return res;
    }
};
