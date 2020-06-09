## here is a dummy version of the likelihood function

# Likelihood
# x is (logmu, logvar)
# args is (bin_bounds, obs_counts)
def log_likelihood(x, *args):
    log_mu = x[0]
    log_var = x[1]
    
    if log_var < 0:
        return 1e10
    
    log_sd = np.sqrt(log_var)
    
    frozen_normal = norm(loc=log_mu, scale=log_sd)
    
    bins = args[0]
    observations = args[1]
    
    bin_probs = [frozen_normal.cdf(bins[0][1]),
                 frozen_normal.cdf(bins[1][1]) - frozen_normal.cdf(bins[1][0]),
                 frozen_normal.cdf(bins[2][1]) - frozen_normal.cdf(bins[2][0]),
                 frozen_normal.cdf(bins[3][1]) - frozen_normal.cdf(bins[3][0]),
                 frozen_normal.cdf(bins[4][1]) - frozen_normal.cdf(bins[4][0]),
                 1 - frozen_normal.cdf(bins[5][0])]
    
    bin_probs.append(1-np.sum(bin_probs))
                
    sum = 0
    
    for i in range(7):
        sum -= observations[i] * np.log(bin_probs[i])
    
    return sum


# to minimize NLL:
for guide:
    est_log_mean, est_log_var = minimize(log_likelihood, (ref_logmean,ref_logvar), args=(bins, obs.loc[guide])).x
