# Concurrenc and Async / Await

## Definitions

### Synchronous
If a program does one task after another, it is called a Synchronous program. Commonly, it is called ´sequential program´, as it performs tasks in a sequence.

- This is like a cook preparing one item completely, and then moving on to the next item. Ex:
    - set the rice for boiling
    - wait
    - wait
    - wait
    - rice cooked!
    - start making curry 

### Asynchronous
If a program performs multiple tasks (not multi-threading), switching from one to another while it is waiting for the current task to respond (ex: i/o operation, api request, writing to disk etc.), then the program is called as an Asynchronous program.

- This is like one cook juggling between multiple dishes on the stove. Ex: Move on to curry, while the rice is boiling.

    This asychronous way of handling the tasks is called ´concurrency´ (different from parallelism). 

## Concurrency vs. Parallelism

In ´concurrency´, a sigle processor is handling multiple tasks. It starts a task, and if it reaches a point where it is waiting for a response from an external dependency, it moves on to another task. After finishing this new task, it will go back to check on the results of the first task.
- This type of processing tasks is useful when there is a lot of waiting involved.

However, ´parallelism´ is performing multiple independent tasks simultaniously using multiple processors. For example, consider a neural net layer of 20 neurons. The CPU has to perform arithematic operation on each neuron with a unique input. Here, there is no waiting business, but just ´execution´ business (Hence, it is also called ´CPU bound´ operation). Here, if each neuron is processed by a unique processor, all the arithematic operations can be performed simultaniously. 
- In this case, concurrency makes no sence. Becuase switching between the tasks doesn't make processing any fast. Even if you switch between the tasks or not, the total amount of processing is the same.
