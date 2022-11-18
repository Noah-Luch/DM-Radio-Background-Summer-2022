HomeDir = './'
DataDir = HomeDir + 'template_data/'

file_dict = {
        '22' : {
            'skymap' : DataDir + 'skymap_22.npy',
            'err_map' : DataDir + '/err_maps/err_map_22.npy',
            'synch_map' :  DataDir + 'synch_22.npy',
            'rms' : 3000.0,
            'calib' : 0.05,
            'resol' : 256,
            'zero_pt' : 5000.0,
        },

        '40' : {
            'skymap' : DataDir + 'lwa_40.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_40.npy',
            'synch_map' :  DataDir + 'synch_40.npy',
            'rms' : 963,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },        

        '45' : {
            'skymap' : DataDir + 'skymap_45.npy',
            'err_map' : DataDir + '/err_maps/err_map_45.npy',
            'synch_map' :  DataDir + 'synch_45.npy',
            'rms' : 300.0,
            'calib' : 0.1,
            'resol' : 64,
            'zero_pt' : 544.0,
        },

        '50' : {
            'skymap' : DataDir + 'lwa_50.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_50.npy',
            'synch_map' :  DataDir + 'synch_50.npy',
            'rms' : 526,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

        '60' : {
            'skymap' : DataDir + 'lwa_60.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_60.npy',
            'synch_map' :  DataDir + 'synch_60.npy',
            'rms' : 365,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

        '70' : {
            'skymap' : DataDir + 'lwa_70.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_70.npy',
            'synch_map' :  DataDir + 'synch_70.npy',
            'rms' : 208,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

        '80' : {
            'skymap' : DataDir + 'lwa_80.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_80.npy',
            'synch_map' :  DataDir + 'synch_80.npy',
            'rms' : 112,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

    
        '408' : {
            'skymap' : DataDir + 'skymap_408.npy',
            'err_map' : DataDir + '/err_maps/err_map_408.npy',
            'synch_map' :  DataDir + 'synch_408.npy',
            'rms' : 1.2,
            'calib' : 0.1,
            'resol' : 512,
            'zero_pt' : 3.0,
        },
        
    
        '1420' : {
            'skymap' : DataDir + 'skymap_1420.npy',
            'err_map' : DataDir + '/err_maps/err_map_1420.npy',
            'synch_map' :  DataDir + 'synch_1420.npy',
            'rms' : 0.017,
            'calib' : 0.05,
            'resol' : 256,
            'zero_pt' : 0.5,
        },
    
        '3150' : {
            'skymap' : DataDir + 'arc2_3150.npy',
            'err_map' : DataDir + '/err_maps/err_map_3150.npy',
            'synch_map' :  DataDir + 'synch_3150.npy',
            'rms' : 0.00901,
            'calib' : 0.0,
            'resol' : 16,
            'zero_pt' : 0.0,
        },
        
        '3410' : {
            'skymap' : DataDir + 'arc2_3410.npy',
            'err_map' : DataDir + '/err_maps/err_map_3410.npy',
            'synch_map' :  DataDir + 'synch_3410.npy',
            'rms' : 0.00765,
            'calib' : 0.0,
            'resol' : 16,
            'zero_pt' : 0.0,
        },

        '7970' : {
            'skymap' : DataDir + 'arc2_7970.npy',
            'err_map' : DataDir + '/err_maps/err_map_7970.npy',
            'synch_map' :  DataDir + 'synch_7970.npy',
            'rms' : 0.0141,
            'calib' : 0.0,
            'resol' : 16,
            'zero_pt' : 0.0,
        },

        '8330' : {
            'skymap' : DataDir + 'arc2_8330.npy',
            'err_map' : DataDir + '/err_maps/err_map_8330.npy',
            'synch_map' :  DataDir + 'synch_8330.npy',
            'rms' : 0.0160,
            'calib' : 0.0,
            'resol' : 16,
            'zero_pt' : 0.0,
        },

        '9720' : {
            'skymap' : DataDir + 'arc2_9720.npy',
            'err_map' : DataDir + '/err_maps/err_map_9720.npy',
            'synch_map' :  DataDir + 'synch_9720.npy',
            'rms' : 0.00596,
            'calib' : 0.0,
            'resol' : 16,
            'zero_pt' : 0.0,
        },

        '10490' : {
            'skymap' : DataDir + 'arc2_10490.npy',
            'err_map' : DataDir + '/err_maps/err_map_10490.npy',
            'synch_map' :  DataDir + 'synch_2326.npy',
            'rms' : 0.00600,
            'calib' : 0.0,
            'resol' : 16,
            'zero_pt' : 0.0,
        }                          
}

'''        '2326' : {
            'skymap' : DataDir + 'skymap_2326.npy',
            'synch_map' :  DataDir + 'synch_2326.npy',
            'rms' : 0.03,
            'calib' : 0.05,
            'resol' : 64
        },
'''

'''        '820' : {
            'skymap' : DataDir + 'skymap_820.npy',
            'synch_map' :  DataDir + 'synch_820.npy',
            'rms' : 0.5,
            'calib' : 0.06,
            'resol' : 256,
            'dowell_rms' : 2.37
        },'''

'''

        '40' : {
            'skymap' : DataDir + 'lwa_40.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_40.npy',
            'synch_map' :  DataDir + 'synch_22.npy',
            'rms' : 963,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },
    

'''



'''


        '50' : {
            'skymap' : DataDir + 'lwa_50.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_50.npy',
            'synch_map' :  DataDir + 'synch_22.npy',
            'rms' : 526,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

        '60' : {
            'skymap' : DataDir + 'lwa_60.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_60.npy',
            'synch_map' :  DataDir + 'synch_22.npy',
            'rms' : 365,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

        '70' : {
            'skymap' : DataDir + 'lwa_70.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_70.npy',
            'synch_map' :  DataDir + 'synch_22.npy',
            'rms' : 208,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

        '80' : {
            'skymap' : DataDir + 'lwa_80.npy',
            'err_map' : DataDir + '/err_maps/lwa_err_80.npy',
            'synch_map' :  DataDir + 'synch_22.npy',
            'rms' : 112,
            'calib' : 0.0,
            'resol' : 256,
            'zero_pt' : 0.0,
        },

'''