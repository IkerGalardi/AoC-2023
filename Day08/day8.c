#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAX_LINE 500
#define MAX_NODES 800
#define NODE_NAME_LEN 3

struct node {
    char name[NODE_NAME_LEN];
    struct node *left;
    struct node *right;
};

static struct node *getnode(struct node *node_list, size_t *n, char name[NODE_NAME_LEN]) {
    for (size_t i = 0; i < *n; i++) {
        if (memcmp(name, node_list[i].name, NODE_NAME_LEN) == 0) {
            return &node_list[i];
        }
    }

    struct node *result = &node_list[*n];
    result->name[0] = name[0];
    result->name[1] = name[1];
    result->name[2] = name[2];
    *n += 1;

    assert(*n < MAX_NODES);
    return result;
}

int main(int argc, char **argv) {
    (void)argc;

    FILE* f = fopen(argv[1], "r");
    assert(f != NULL);

    size_t n_nodes = 0;
    struct node node_list[MAX_NODES] = {0};
    char *commands = NULL;

    enum {
        STATE_COMMAND_LINE,
        STATE_BLANK_LINE,
        STATE_GRAPH_LINE
    } state = STATE_COMMAND_LINE;
    size_t size = 0;
    char *linebuff = NULL;
    while(getline(&linebuff, &size, f) > 0) {
        if (state == STATE_COMMAND_LINE) {
            size_t linelen = strlen(linebuff);
            commands = malloc(linelen + 1);
            strcpy(commands, linebuff);
            state = STATE_BLANK_LINE;
        } else if (state == STATE_BLANK_LINE) {
            state = STATE_GRAPH_LINE;
            continue;
        } else if (state == STATE_GRAPH_LINE) {
            char thisnodename[NODE_NAME_LEN];
            char leftnodename[NODE_NAME_LEN];
            char rightnodename[NODE_NAME_LEN];

            // NOTE: The line format is assumed to be:
            //       AAA = (BBB, CCC)
            thisnodename[0] =  linebuff[0];
            thisnodename[1] =  linebuff[1];
            thisnodename[2] =  linebuff[2];
            leftnodename[0] =  linebuff[7];
            leftnodename[1] =  linebuff[8];
            leftnodename[2] =  linebuff[9];
            rightnodename[0] = linebuff[12];
            rightnodename[1] = linebuff[13];
            rightnodename[2] = linebuff[14];


            struct node *currnode = getnode(node_list, &n_nodes, thisnodename);
            struct node *leftnode = getnode(node_list, &n_nodes, leftnodename);
            struct node *rightnode = getnode(node_list, &n_nodes, rightnodename);
            
            currnode->left = leftnode;
            currnode->right = rightnode;
        }
    }
    assert(commands != NULL);
    assert(n_nodes != 0);

    for(size_t i = 0; i < n_nodes; i++) {
            char *thisnodename = node_list[i].name;
            char *leftnodename = node_list[i].left->name;
            char *rightnodename = node_list[i].right->name;
        printf("%c%c%c = (%c%c%c, %c%c%c)\n",
               thisnodename[0], thisnodename[1], thisnodename[2],
               leftnodename[0], leftnodename[1], leftnodename[2],
               rightnodename[0], rightnodename[1], rightnodename[2]);
    }

    int i = 0;
    int nsteps = 1;
    char startname[NODE_NAME_LEN] = {'A', 'A', 'A'};
    struct node *thisnode = getnode(node_list, &n_nodes, startname);
    while(1) {
        printf("Step %d: %c%c%c", nsteps, thisnode->name[0], thisnode->name[1], thisnode->name[2]);
        if (commands[i] == 'L') {
            thisnode = thisnode->left;
        } else if (commands[i] == 'R') {
            thisnode = thisnode->right;
        } else {
            printf("BERGA");
        }

        printf(" -> %c%c%c\n", thisnode->name[0], thisnode->name[1], thisnode->name[2]);

        if (thisnode->name[0] == 'Z' && thisnode->name[1] == 'Z' && thisnode->name[2] == 'Z') {
            break;
        }

        nsteps++;
        i++;
        if (commands[i] == '\n') {
            i = 0;
        }
    }

    printf("Took %d steps\n", nsteps);

    fclose(f);
}