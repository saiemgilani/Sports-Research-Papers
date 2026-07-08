n.trials = 20
n.success = 9
n.samples = 1000
streak.pat = c(1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0)
nstreak.pat = c(0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0)
rand.pat = c(0,0,0,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0)

n.runs = c()

for (i in 1:n.samples){
    n.runs[i] = length(rle(sample(nstreak.pat))$length)
}

runs.streak.pat = length(rle(streak.pat)$length)
runs.nstreak.pat = length(rle(nstreak.pat)$length)
runs.rand.pat = length(rle(rand.pat)$length)

empirical.p.val.streak.pat = length(which(n.runs<=runs.streak.pat))/n.samples
empirical.p.val.nstreak.pat = length(which(n.runs>=runs.nstreak.pat))/n.samples
empirical.p.val.nrand.pat = length(which(n.runs<=runs.rand.pat))/n.samples

z.score.streak.pat = (runs.streak.pat-mean(n.runs))/sd(n.runs)
z.score.nstreak.pat = (runs.nstreak.pat-mean(n.runs))/sd(n.runs)
z.score.rand.pat = (runs.rand.pat-mean(n.runs))/sd(n.runs)
