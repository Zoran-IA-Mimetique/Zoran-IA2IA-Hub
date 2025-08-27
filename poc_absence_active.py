# Bayesian toy: P(event) from absence of evidence
# P(Evidence|Event)=p1, P(Evidence|¬Event)=p0 ; observe no evidence
p_event=0.5; p1=0.8; p0=0.1
# P(noE|Event)=1-p1 ; P(noE|¬Event)=1-p0
num = (1-p1)*p_event
den = (1-p1)*p_event + (1-p0)*(1-p_event)
print(round(num/den,3))