import numpy as np
from numpy.random import Generator, PCG64, SeedSequence


class MonteCarloManager:
    

    def __init__(self, base_bit_gen: PCG64, scen_block_size, rn_locs: {}, rn_size = 100):
        
        self.base_bit_gen = base_bit_gen
        self.base_state = self.base_bit_gen.state

        self.scen_block_size = scen_block_size
        self.rn_locs = rn_locs
        self.rn_size = rn_size
        self.rn_generators = {rn:None for rn in rn_locs}

    def get_rng(self, rn):
        
        rng = self.rn_generators[rn]
        if rng is None:

            self.base_bit_gen.state = self.base_state
            self.base_bit_gen.advance(self._get_advance_size(self.rn_locs[rn]))
            bit_gen = PCG64()
            bit_gen.state = self.base_bit_gen.state
            
                        
            self.rn_generators[rn] = Generator(bit_gen)
            rng = self.rn_generators[rn]

        return rng

    def _get_advance_size(self, loc):
        return self.rn_size * self.scen_block_size * loc


if __name__ == '__main__':

    scen_block_size = 10000
    num_rns = 1000
    num_scens = 10000
    num_scens_for = 100

    ss = SeedSequence(123456)
    def get_res():

        base_bit_gen = np.random.PCG64(ss)
        rn_locs = {str(i):i for i in range(num_rns)}
        mcm = MonteCarloManager(base_bit_gen, num_scens, rn_locs)
        kw_res = {}
        n_s_b = [num_scens_for] * int(num_scens / num_scens_for)
        for b in range(len(n_s_b)):
            n_scen_b = n_s_b[b]

            rn_shuffled = list(rn_locs.keys())
            np.random.shuffle(rn_shuffled)

            for rn in rn_shuffled:
                if b == 0:
                    kw_res[rn] = []
                rng_rn = mcm.get_rng(rn)
                rx = rng_rn.standard_normal(n_scen_b)
                kw_res[rn].append(rx)
        
        for k in kw_res:
           kw_res[k] = np.hstack(kw_res[k])

        return kw_res

    res1 = get_res()
    res2 = get_res()

    print('testing...')
    success = True
    for k in res1:
        d = np.max(np.abs(res1[k] - res2[k]))

        if d > 0.0:
            print('failed: Different results for ' + k + ':' + str(d))
            success = False
        
    if success: 
        print('success')
