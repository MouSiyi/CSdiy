 ## Intro 
Time-to-event/failure-time data is a new data type(neither categorical nor continuous), and thus requires new approaches to statistical analysis.
- New summary statistics(Moments donot work)
- New methods for visualizing
- New methods for inference
- New methods for modeling

Why it's new data type?
Time-to-event data cannot be seen as complete information(categorical or continuous), as the event may not happen or the expense to wait is too high.      
It cannot be seen as missing data, as some information is wasted.   
Why using new methods?
It is difficult for parametric distributions  to describe survival data, and many assumptions of parametric approaches are open to debate.(其实不是特别理解)      
Moments-based statistics are often impossible to get and inadequate for describing unusual distributions.    

Therefore nonparametric or semiparametric approaches tend to more widely used in Survival Analysis.
It's also natural to think about survival times conditionally: e.g. the risk of death given that an individual has survived up until a certain age.(*The hazard function*)


## General Notation
- $T$ : the time from some specified origin until the event
- We donot always observe $T$; we observe $\{t_i, \delta_i, x_i\}_{i=1}^n$
  - $t_i$ : the follow-up time; $t_i = min\{\widetilde T_i, C_i\}$
  - $\delta_i$ : indicator for whether the event was observed; $\delta = I\{ \widetilde T_i\le C_i\}$ 
  - $x_i$: explanatory variables
So it can be regarded that the response is $(t_i, \delta_i)$

![[pic1.png]]
![[pic2.png]]
![[pic3.png]]
![[pic4.png]]
## Relationship between discrete and continuous cases

