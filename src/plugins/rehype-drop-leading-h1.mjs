/**
 * 删除 markdown 正文中的首个 <h1>。
 *
 * 背景：vehicles / brands / docs 三个模板的 hero 已经把页面标题渲染为 H1；
 * 而 517 个车型 + 72 个品牌 + 13 个文档的 markdown 正文又都以「# 标题」开头，
 * 导致同一页面出现两个 H1（全站 SEO 体检命中 603 页）。
 * 正文其余标题（h2/h3…）与全部内容不受影响，无 TOC 依赖这些锚点。
 */
export default function rehypeDropLeadingH1() {
  return (tree) => {
    const walk = (parent) => {
      if (!parent || !Array.isArray(parent.children)) return false;
      for (let i = 0; i < parent.children.length; i++) {
        const node = parent.children[i];
        if (node.type === 'element' && node.tagName === 'h1') {
          parent.children.splice(i, 1);
          return true;
        }
        if (walk(node)) return true;
      }
      return false;
    };
    walk(tree);
  };
}
