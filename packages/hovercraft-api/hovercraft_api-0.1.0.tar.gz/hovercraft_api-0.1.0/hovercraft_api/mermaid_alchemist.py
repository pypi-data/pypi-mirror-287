import re
from loguru import logger
from art import *

class MermaidFusionMaster:
    def __init__(self):
        logger.info("MermaidFusionMasterを初期化しています")

    def orchestrate_fusion(self, html_path, md_path, output_path):
        print(text2art(">>    MermaidFusionMaster","rnd-medium"))
        logger.info("Mermaid統合プロセスを開始します")
        html_content = self._acquire_content(html_path)
        md_content = self._acquire_content(md_path)

        if html_content and md_content:
            mermaid_essence = self._extract_mermaid_essence(md_content)
            if mermaid_essence:
                enhanced_html = self._infuse_mermaid_content(html_content, mermaid_essence)
                enhanced_html = self._empower_with_mermaid_scripts(enhanced_html)
                self._materialize_fusion(output_path, enhanced_html)
                logger.success("Mermaid統合プロセスが見事に完了しました")
            else:
                logger.error("Mermaidのエッセンスが見つからず、融合プロセスを中断します")
        else:
            logger.error("必要な素材の取得に失敗し、融合プロセスを中断します")

    def _acquire_content(self, file_path):
        logger.info(f"{file_path}の内容を取得します")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            logger.success(f"{file_path}の内容取得に成功しました")
            return content
        except Exception as e:
            logger.error(f"{file_path}の取得中に障害が発生しました: {str(e)}")
            return None

    def _materialize_fusion(self, file_path, content):
        logger.info(f"融合結果を{file_path}に具現化します")
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            logger.success(f"融合結果の具現化が完了しました: {file_path}")
        except Exception as e:
            logger.error(f"融合結果の具現化中に障害が発生しました: {str(e)}")

    def _extract_mermaid_essence(self, md_content):
        logger.info("Mermaidのエッセンスを抽出します")
        mermaid_match = re.search(r'```mermaid\n(.*?)\n```', md_content, re.DOTALL)
        if mermaid_match:
            logger.success("Mermaidのエッセンス抽出に成功しました")
            return mermaid_match.group(1)
        else:
            logger.warning("Mermaidのエッセンスが見つかりませんでした")
            return None

    def _infuse_mermaid_content(self, html_content, mermaid_essence):
        logger.info("HTMLにMermaidのエッセンスを注入します")
        pattern = r'<p>Content block expected for the "code" directive; none found.</p>\s*<pre class="highlight ">.. code:: mermaid\s*</pre>.*?</dl>'
        infusion = f'''<div class="mermaid">
{mermaid_essence}
</div>'''
        enhanced_html = re.sub(pattern, infusion, html_content, flags=re.DOTALL)
        logger.success("Mermaidエッセンスの注入が完了しました")
        return enhanced_html

    def _empower_with_mermaid_scripts(self, html_content):
        logger.info("HTMLをMermaidの力で強化します")
        mermaid_enchantment = '''
<script src="https://unpkg.com/mermaid/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({
      startOnLoad: true, 
      theme: 'default'
  });
</script>
'''
        head_end = html_content.find('</head>')
        if head_end != -1:
            empowered_html = html_content[:head_end] + mermaid_enchantment + html_content[head_end:]
            logger.success("Mermaidの力による強化が完了しました")
            return empowered_html
        else:
            logger.error("HTMLの頭部が見つからず、強化に失敗しました")
            return html_content

def main():
    logger.info("Mermaid融合の儀式を開始します")
    fusion_master = MermaidFusionMaster()
    fusion_master.orchestrate_fusion(
        'example/hovercraft_assets/index.html',
        'example/hovercraft_assets/test_output_slides.md',
        'example/hovercraft_assets/index2.html'
    )

if __name__ == "__main__":
    main()
