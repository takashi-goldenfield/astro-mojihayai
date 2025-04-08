import TreeView from "../TreeView";
import IconCategory from "~icons/tabler/category";
import IconFolderFill from "~icons/mingcute/folder-fill";
import IconGridFill from "~icons/mingcute/grid-fill";
import IconArrowRight from "~icons/mingcute/arrow-right-fill";

interface TerminalTreeNode {
  label: string;
  url: string;
  count: number;
}

interface InternalTreeNode {
  label: string;
  url?: string;
  count: number;
  children: TreeNode[];
}

type TreeNode = InternalTreeNode | TerminalTreeNode;

function addTreeNode(
  node: TreeNode,
  path: string[],
  count: number,
  url: string
) {
  if (path.length) {
    const label = path[0];
    if ("children" in node) {
      // is internal node
      const child = node.children.find((child) => child.label === label);
      if (child) {
        child.count += count;
        if (path.length === 1) {
          child.url = url;
        } else {
          addTreeNode(child, path.slice(1), count, url);
        }
      } else {
        if (path.length === 1) {
          const newNode = {
            // create terminal node
            label,
            count,
            url,
          };
          node.children.push(newNode);
        } else {
          const newNode = {
            // create internal node
            label,
            count,
            children: [],
          };
          node.children.push(newNode);
          addTreeNode(newNode, path.slice(1), count, url);
        }
      }
    }
  }
}

function parseCategoriesToTree(
  categories: {
    label: string;
    count: number;
    url: string;
  }[]
) {
  const tree = {
    label: "root",
    count: 0,
    children: [],
  } as InternalTreeNode;
  for (const category of categories) {
    const path = category.label.split("/");
    addTreeNode(tree, path, category.count, category.url);
  }
  return tree;
}

function renderSubtree(
  tree: InternalTreeNode,
  expandDepth: number,
  depth: number
) {
  return (
    <TreeView.Item
      label={
        tree.url ? (
          <a
            href={tree.url}
            className="hover:font-bold group"
            onClick={(e) => e.stopPropagation()}
          >
            {tree.label}
            <IconArrowRight
              className="inline transition opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0"
              width={12}
              height={12}
            />
          </a>
        ) : (
          tree.label
        )
      }
      icon={<IconFolderFill width={15} height={15} />}
      endIcon={<div className="text-xs px-1">[{tree.count}]</div>}
      defaultExpanded={depth <= expandDepth}
      key={tree.label}
    >
      {tree.children.map((child) => {
        if ("children" in child) {
          return renderSubtree(child, expandDepth, depth + 1);
        }
        return (
          <TreeView.Item
            label={
              <a href={child.url} className="hover:font-bold group">
                {child.label}
                <IconArrowRight
                  className="inline transition opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0"
                  width={12}
                  height={12}
                />
              </a>
            }
            icon={<IconGridFill width={15} height={15} />}
            endIcon={<div className="text-xs px-1">[{child.count}]</div>}
            key={child.label}
          />
        );
      })}
    </TreeView.Item>
  );
}

export interface CategoryTreeProps {
  categories: {
    label: string;
    url: string;
    count: number;
  }[];
  expandDepth?: number;
}

export default function CategoryTree({
  categories,
  expandDepth = 2,
}: CategoryTreeProps) {
  const tree = parseCategoriesToTree(categories);
  return (
    <div>
      <h2 className="font-bold text-lg flex items-center p-2">
        <IconCategory className="w-5 h-5 mr-1" />
        Labels
      </h2>
      <TreeView className="plate-bg border-highlight p-2 rounded-xl overflow-hidden">
        {tree.children.map((child) => {
          if ("children" in child) {
            return renderSubtree(child, expandDepth, 1);
          }
          return (
            <TreeView.Item
              label={
                <a href={child.url} className="hover:font-bold group">
                  {child.label}
                  <IconArrowRight
                    className="inline transition opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0"
                    width={12}
                    height={12}
                  />
                </a>
              }
              icon={<IconGridFill width={15} height={15} />}
              endIcon={<div className="text-xs px-1">[{child.count}]</div>}
              key={child.label}
            />
          );
        })}
      </TreeView>
    </div>
  );
}
