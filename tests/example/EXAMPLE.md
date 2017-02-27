# ResourceServerPy - Example Paths

We have here a pretend JS library, as such:

```
.
├── agents
│   └── rennet.js
└── food
    ├── fridge
    │   ├── lemon.js
    │   ├── milk.js
    │   └── toppings
    │       ├── cheese.js
    │       ├── ketchup.js
    │       └── pepperoni.js
    ├── hamburger.js
    └── pizza.js
```

We should be able to use the classpath, ```examples/food``` to get the resource ```com.sleepyjay.hamburger```. Hamburger requires cheese. Cheese requires a curdler. If we don't include the ```examples/agents```, we would get ```com.sleepyjay.lemon``` (because it provides the resource named ```com.sleepyjay.agents.curdler```). However, if we include the ```examples/agents``` classpath (after ```examples/food```), ```com.sleepyjay.rennet``` will get pulled instead (to satisfy the curdler requirement). 