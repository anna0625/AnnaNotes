<style>
.highlight1{
    color: #EAC100 !important;
}
.highlight2{
    color: #AFAF61;
}
.comingsoon{
    color: red;
}
</style>

## Git Notebook
---

Stay here or [Go Back to Home Page](../index.md).<br/>
It includs some problems what you might meet and some solutions here.<br/>
Here also will include some basic knowledge about how to do version control with github, and I will do my best to write notes faster. Please be patient with me. Thank you!

<br/>


## Problems and Solutions
---

### Problem 1

If you meet this on your terminal..
* Please, commit your changes or stash them before you can merge.  
Aborting

Here is a solution that would be helpful.
```
% git stash
% git pull
% git stash pop
```

### Problem 2

If you meet this on your terminal..
* fatal: refusing to merge unrelated histories

Here is a solution that would be helpful.
```
% git pull origin master --allow-unrelated-histories
```
or
```
% git merge origin master --allow-unrelated-histories
```