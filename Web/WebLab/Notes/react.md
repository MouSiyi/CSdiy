### React

Your app can be divided into a tree of components.
A framework that lets you divide up your website into reusable components.  
Each component is kind of like a 'custom HTML tag' that you define, which is a function with props as the input and returns JSX.

#### Props

Inputs passed from a parent to a child component.
Props are immutable!

ex.:
<Post name="post" text= />

#### State

Private information maintained by a component.
Mutable.

We pass props from parent to child conponent.

Allows our skeleton to render comments with content.

State keeps track of private information that can be changed and influence how your apps renders.

Declare state variables with:
const [sth, setSth] = useState(initialValue)

React uses className instead of class for css styles.
