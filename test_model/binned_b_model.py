import numpy as np
import healpy as hp
from MyUnits import *

HomeDir = './'
DataDir = HomeDir + 'template_data/'
# Useful functions 
from fake_dict import fake_dict




# Get rid of slice |b| < b_min degrees
def remove_sky(skymap, b_min, l_min = 0, is_nest = False):
    nside = hp.npix2nside(len(skymap))
    skymap_cp = np.copy(skymap)
    lon, lat = hp.pix2ang(nside, np.arange(len(skymap_cp)), nest = is_nest, lonlat = True)
    skymap_cp[np.abs(lat) < b_min] = np.nan
    skymap_cp[lon < l_min] = np.nan
    skymap_cp[lon > 360 - l_min] = np.nan
    #print(len(skymap_cp[~np.isnan(skymap_cp)]))
    return skymap_cp

# Brightness temperature of CMB
def cmb_bt(freq):
    return (2.72548 * Kelvin) *(2 * np.pi * freq/(2.72548 * Kelvin)) /(np.exp(2 * np.pi * freq/(2.72548 * Kelvin))-1)

## Masking 

# minimum latitude and longitudes we consider
B_MIN = 10
L_MIN = 0

# initial resolution of fake_data
i_res = 64 

# resolution of fit
f_res = 16

npix = hp.nside2npix(i_res)
f_res_pix = hp.nside2npix(f_res)

pix_list = np.arange(f_res_pix, dtype = 'float')
pix_list = remove_sky(pix_list, B_MIN, L_MIN)
pix_list = pix_list[~np.isnan(pix_list)]
pix_list = np.asarray(pix_list, dtype = 'int')

num_pix_r = len(pix_list[~np.isnan(pix_list)]); pix_list


#number of b bins per hemisphere
num_b = 2
b_bins = np.arange(-90, 90, 180/(num_b))
# latitudes
_, lat = hp.pix2ang(f_res, pix_list, nest = False, lonlat = True)
# b bin assignments
b_assgn = np.digitize(lat, bins = b_bins)
#b_bins = np.concatenate((b_bins, [90]))
b_bins, b_assgn

csc_i = 1/np.sin(np.abs(lat) * degree)

# load source template 

pt_src = np.load(DataDir + 'pt_src.npy')
vlbi_src = np.load(DataDir + 'vlbi_src_mask.npy')
pt_src_dg = hp.ud_grade(pt_src, f_res)
vlbi_src_dg = hp.ud_grade(vlbi_src, f_res)

nu_ = np.asarray([float(n) for n in nu_list]) / 310.0 # reference frequency is 310 MHz
nu_arr = np.broadcast_to(nu_, (len(csc_i),len(nu_list))).T

# dimensionality of our problem : 2 + 2 * num_b

ndim = 2 + 2 * num_b + 1
print ('ndim = ' + str(ndim))


def loglike(x):
    # extragalactic parameters
    T_CMB =  x[0] #2.722
    T_E =  x[1] #30.4 #
    beta_E = x[2] #-2.58 # 
    
    # galactic parameters
    T_G  =  x[3 : (2 + num_b)+1] #np.asarray([9.65,8.06]) #
    
    beta_G = x[(2 + num_b)+1 : (2 + 2 * num_b)+1] # np.asarray([-2.58, -2.56])#
    
    # isotropic component
    TE_i = T_E * np.ones(num_pix_r) 
    nu_beta_E = np.power(nu_, beta_E)
    TE_i_q = np.outer(nu_beta_E, TE_i)

    # galactic component
    TG_csc_i = T_G[b_assgn-1] * csc_i
    nu_beta_G = np.power(nu_arr, beta_G[b_assgn-1])
    TG_i_q = TG_csc_i * nu_beta_G
    
    # residual array
    res_arr = inv_cov_r * (skymaps_r - (T_CMB + TE_i_q + TG_i_q))**2
    
    # contract over pixel and map indices
    return -0.5 * np.einsum('qi->', res_arr)


#instiantiate array with priors

scale = np.zeros(ndim) # size of prior
shift = np.zeros(ndim) # location of prior

scale[0] = 4
scale[1] = 1500
scale[2] = 2.8
scale[3: (2 + num_b)+1] = 50
scale[(2 + num_b)+1 : (2 + 2 * num_b)+1] = 2.7

shift[0] = 0
shift[1] = 0
shift[2] = -2.8
shift[3: (2 + num_b)+1] = 0
shift[(2 + num_b)+1 : (2 + 2 * num_b)+1] = -2.7

def ptform(u):
    return scale * u + shift