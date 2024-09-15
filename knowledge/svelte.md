# Svelte User Manual

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Creating Your First Svelte App](#creating-your-first-svelte-app)
4. [Components](#components)
5. [Reactivity](#reactivity)
6. [Props and Component Communication](#props-and-component-communication)
7. [Events](#events)
8. [Bindings](#bindings)
9. [Conditional Rendering](#conditional-rendering)
10. [Loops](#loops)
11. [Stores](#stores)
12. [Lifecycle Hooks](#lifecycle-hooks)
13. [Conclusion](#conclusion)

---

## Introduction

Svelte is a modern JavaScript framework for building user interfaces. Unlike traditional frameworks that run in the browser, Svelte compiles your code to highly efficient JavaScript at build time, resulting in faster load times and improved performance.

**Key Features:**

- **No Virtual DOM:** Directly updates the DOM, leading to efficient rendering.
- **Compile-Time Optimizations:** Converts your components into imperative code.
- **Reactivity:** Reactive assignments and statements for state management.
- **Simplicity:** Minimal boilerplate with a focus on developer experience.

---

## Installation

To get started with Svelte, you'll need to have [Node.js](https://nodejs.org/) installed.

### Using degit

Create a new project using the template:

```bash
npx degit sveltejs/template my-svelte-app
cd my-svelte-app
npm install
npm run dev
```

- **npx degit sveltejs/template my-svelte-app:** Clones the starter template.
- **npm install:** Installs dependencies.
- **npm run dev:** Starts the development server.

---

## Creating Your First Svelte App

After running the development server, open [http://localhost:5000](http://localhost:5000) to see your app.

### File Structure

- `public/`: Static assets.
- `src/`: Source code.
  - `App.svelte`: Main component.

---

## Components

Svelte applications are built from components, which are reusable, self-contained blocks of code.

### Basic Component Structure

```svelte
<script>
  // JavaScript logic
</script>

<style>
  /* Component-specific styles */
</style>

<!-- Markup -->
<div>
  <h1>Hello, Svelte!</h1>
</div>
```

- `<script>`: Contains the component's logic.
- `<style>`: Scoped CSS styles.
- Markup: HTML-like syntax.

---

## Reactivity

Svelte offers a simple reactivity model using assignments.

### Reactive Assignments

```svelte
<script>
  let count = 0;

  function increment() {
    count += 1;
  }
</script>

<button on:click="{increment}">
  Count: {count}
</button>
```

- **Reactivity:** Updating `count` automatically updates the UI.

### Reactive Statements

```svelte
<script>
  let a = 2;
  let b = 3;

  $: sum = a + b;
</script>

<p>The sum is {sum}</p>
```

- **$: sum = a + b;**: Recalculates `sum` whenever `a` or `b` changes.

---

## Props and Component Communication

Pass data to child components using props.

### Parent Component

```svelte
<ChildComponent message="Hello from parent!" />
```

### Child Component (`ChildComponent.svelte`)

```svelte
<script>
  export let message;
</script>

<p>{message}</p>
```

- **export let message;**: Declares `message` as a prop.

---

## Events

Components can dispatch events to communicate with parents.

### Child Component

```svelte
<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  function send() {
    dispatch('message', { text: 'Hello Parent!' });
  }
</script>

<button on:click="{send}">Send Message</button>
```

### Parent Component

```svelte
<ChildComponent on:message="{handleMessage}" />

<script>
  function handleMessage(event) {
    console.log(event.detail.text);
  }
</script>
```

- **dispatch('message', { text: '...' });**: Sends an event.
- **on:message="{handleMessage}"**: Listens for the event.

---

## Bindings

Two-way data binding allows synchronization between variables and inputs.

### Input Binding

```svelte
<script>
  let name = '';
</script>

<input bind:value="{name}" placeholder="Enter your name" />
<p>Hello, {name}!</p>
```

- **bind:value="{name}"**: Binds the input value to the `name` variable.

---

## Conditional Rendering

Display content conditionally using `{#if}` blocks.

```svelte
<script>
  let loggedIn = false;
</script>

{#if loggedIn}
  <p>Welcome back!</p>
{:else}
  <p>Please log in.</p>
{/if}
```

- **{#if}...{:else}...{/if}:** Conditional rendering syntax.

---

## Loops

Render lists using `{#each}` blocks.

```svelte
<script>
  let items = ['Apple', 'Banana', 'Cherry'];
</script>

<ul>
  {#each items as item}
    <li>{item}</li>
  {/each}
</ul>
```

- **{#each items as item}:** Iterates over `items`.

---

## Stores

Stores provide a way to share reactive data between components.

### Writable Store

```javascript
// store.js
import { writable } from 'svelte/store';

export const count = writable(0);
```

### Using the Store

```svelte
<script>
  import { count } from './store.js';
</script>

<button on:click="{() => count.update(n => n + 1)}">
  Count: {$count}
</button>
```

- **$count:** Auto-subscription to the store's value.

---

## Lifecycle Hooks

Respond to component lifecycle events.

### onMount

```svelte
<script>
  import { onMount } from 'svelte';

  onMount(() => {
    console.log('Component mounted');
  });
</script>
```

- **onMount:** Runs after the component is added to the DOM.

### Other Hooks

- **beforeUpdate:** Before the DOM updates.
- **afterUpdate:** After the DOM updates.
- **onDestroy:** Before the component is removed.

---

## Conclusion

Svelte simplifies building web applications by offering a compiler that optimizes your code. Its intuitive reactivity, component-based architecture, and efficient performance make it a powerful tool for modern web development.

---

**References:**

- Official Documentation: [https://svelte.dev/docs](https://svelte.dev/docs)
- Tutorial: [https://svelte.dev/tutorial](https://svelte.dev/tutorial)
- API Reference: [https://svelte.dev/docs#API_reference](https://svelte.dev/docs#API_reference)