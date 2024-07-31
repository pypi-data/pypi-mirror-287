##########
#
# funcs.py
#
#
# Author: Clinton H. Durney
# Email: cdurney@math.ubc.ca
#
# Last Edit: 11/8/19
##########


from numba import jit

from scipy.spatial import ConvexHull
import numpy as np



@jit(nopython=True, cache=True, inline='always')
def euclidean_distance(A, B):
    '''Calculate the Euclidean distance from point A to B'''
    
    d=B-A
    return np.sqrt(np.sum(d*d))

@jit(nopython=True, cache=True, inline='always')
def unit_vector(A,B):
    '''Calculate the unit vector pointing from A to B'''

    dist = euclidean_distance(A,B)

    return (B-A)/dist


@jit(nopython=True, cache=True, inline='always')
def unit_vector_and_dist(A, B):
    # Calculate the unit vector from A to B, and return the distance as well

    dist = euclidean_distance(A, B)

    return (B-A)/dist, dist

def unit_vector_2D(A,B):
    return unit_vector(A,B)[:2]



def convex_hull_volume(pts):
    return ConvexHull(pts).volume


@jit(nopython=True, cache=True, inline='always')
def cross33(a,b):
    # cross product between two 3-vectors
    return np.array([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]])

@jit(nopython=True, cache=True, inline='always')
def cross3Mat(a,b):
    #cross product between a vector and an Nx3 matrix
    out = np.zeros((b.shape))
    for i in range(0,b.shape[0]):
        out[i,0]=a[1]*b[i,2]-a[2]*b[i,1]
        out[i,1]=a[2]*b[i,0]-a[0]*b[i,2]
        out[i,2]=a[0]*b[i,1]-a[1]*b[i,0]

    return out

@jit(nopython=True, cache=True, inline='always')
def crossMatMat(a,b):
    # pair-wise cross products of two Nx3 matrices
    out = np.zeros((b.shape))
    for i in range(0,b.shape[0]):
        out[i,0]=a[i,1]*b[i,2]-a[i,2]*b[i,1]
        out[i,1]=a[i,2]*b[i,0]-a[i,0]*b[i,2]
        out[i,2]=a[i,0]*b[i,1]-a[i,1]*b[i,0]

    return out    



@jit(nopython=True, cache=True, inline='always')
def triangle_area_and_vector(pos_side):
    
    A_alpha = triangle_area_vector(pos_side)
    return np.linalg.norm(A_alpha), A_alpha
    

@jit(nopython=True, cache=True, inline='always')
def triangle_area_vector(pos_side):
    '''
    Computes the area vector normal to a triagle from its vertex positions.

    Args:
        pos_side: a 3x3 `numpy.ndarray` of triangle vertex positions.

    Returns:
        A `numpy.ndarray` of size (3,), the area vector.
    '''
    inds=np.array([2,0,1])
    A_alpha = np.sum(crossMatMat(pos_side,pos_side[inds]),axis=0)/2
    return A_alpha

@jit(nopython=True, cache=True, inline='always')
def triangle_areas_and_vectors(pos_side):

    A_alpha = triangle_area_vectors(pos_side)
    
    return np.array([np.linalg.norm(v) for v in A_alpha]), A_alpha

@jit(nopython=True, cache=True, inline='always')
def triangle_area_vectors(pos_side) -> np.ndarray:
    
    inds=np.array([2,0,1])
    A_alpha = 0.5*np.sum(np.cross(pos_side,pos_side[:,inds,:]), axis=1)
    
    return A_alpha




@jit(nopython=True, cache=True, inline='always')
def raycast_from_point_to_plane_along_direction(y, x1, x2, v, d):
    '''Performs a raycast from a point `y` along the direction `d` to a plane defined by the points `x1` and `x2` as well as a vector `v`.
    
    This code works in arbitary dimensions, and requires that `x2-x1` and `v` are not co-linear.

    Returns a 2-tuple with the intersection point as the first item, and the distance as the second.
    '''
    w=unit_vector(x1, x2)
    nhat=cross33(v/np.linalg.norm(v),w)
    denominator=np.dot(nhat,d)
    if denominator!=0.0:
        ell=-np.dot(nhat, y-x1)/denominator
        return (y+ell*d, np.abs(ell))
    else:#the plane is co-linear with d
        if np.abs(np.dot(nhat, y-x1))<1e-14: #the point is already on the plane
            return (y,0)
        else: #the point is off the plane, so there is no intersection
            out=np.empty(y.shape)
            out[:]=np.nan
            return (out, np.nan)

@jit(nopython=True, cache=True, inline='always')
def distance_from_faceplane_along_direction(y, x1, x2, v, d):
    '''Finds the distance from a point `y` along the direction `d` to a face plane defined by the vertices `x1` and `x2` as well as a vector `v`.
        
        This code works in arbitary dimensions, and requires that `x2-x1` and `v` are not co-linear.

        Performs a raycast to the plane along `d` and checks if the intersection point is between `x1` and `x2`, i.e., on the face.

        If the intersection point is not on the face, then we return NaN.

        Returns a non-negative float or NaN.
    '''
 
    y_plane, dist_plane = raycast_from_point_to_plane_along_direction(y, x1, x2, v, d)
    w=unit_vector(x1, x2)

    #check if the intersection point is "between" `x1` and `x2`
    #if the point is between `x1` and `x2`, the dot products of the displacment will have opposite sign 
    dot1=np.dot(y_plane-x1,w)
    dot2=np.dot(y_plane-x2,w)
    if dot1*dot2<0:
        return dist_plane
    else: #if intersection point is not on the face then we return NaN
        return np.nan
    
@jit(nopython=True, cache=True, inline='always')
def projected_distance_from_faceplane_along_direction( proj, y, x1, x2, v, d):
    '''Finds the projected distance from a point `y` to a face plane along the direction `d`, as measured along a projection axis `proj`.

        The face plane is defined by the vertices `x1` and `x2` as well as a vector `v`.    
    
        This code works in arbitary dimensions, and requires that `x2-x1` and `v` are not co-linear.

        Performs a raycast to the plane along `d` and checks if the intersection point is between `x1` and `x2`, i.e., on the face.

        If the intersection point is not on the face, then we return NaN.

        Returns a non-negative float or NaN.
    '''
 
    y_plane, dist_plane = raycast_from_point_to_plane_along_direction(y, x1, x2, v, d)
    w=unit_vector(x1, x2)

    #check if the intersection point is "between" `x1` and `x2`
    #if the point is between `x1` and `x2`, the dot products of the displacment will have opposite sign 
    dot1=np.dot(y_plane-x1,w)
    dot2=np.dot(y_plane-x2,w)
    if dot1*dot2<0:
        return np.abs(np.dot(y_plane-y, proj/np.linalg.norm(proj)))
    else: #if intersection point is not on the face then we return NaN
        return np.nan
    

xhat=np.array([1.0,0.0,0.0])
yhat=np.array([0.0,1.0,0.0])
zhat=np.array([0.0,0.0,1.0])