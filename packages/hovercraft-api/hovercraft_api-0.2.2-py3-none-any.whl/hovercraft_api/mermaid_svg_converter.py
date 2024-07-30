import os
import subprocess
import re
import uuid
from loguru import logger
from art import *
import html
import shutil

class MermaidSVGConverter:
    def __init__(self, css_file=None):
        logger.info("MermaidSVGConverterを初期化しています")
        self.mmdc_path = self._find_mmdc()
        self.css_file = css_file

    def _find_mmdc(self):
        mmdc_path = shutil.which('mmdc')
        if mmdc_path:
            logger.info(f"mmdcコマンドが見つかりました: {mmdc_path}")
            return mmdc_path
        else:
            logger.error("mmdcコマンドが見つかりません。PATHを確認してください。")
            return None

    def convert_html_mermaid_to_svg(self, input_html_path, output_html_path):
        print(text2art(">>    MermaidSVGConverter", "rnd-medium"))
        logger.info("Mermaid to SVG変換プロセスを開始します")
        
        if not self.mmdc_path:
            logger.error("mmdcコマンドが利用できないため、変換プロセスを中断します")
            return

        input_dir = os.path.dirname(input_html_path)
        svg_dir = os.path.join(input_dir, "svg")
        os.makedirs(svg_dir, exist_ok=True)
        logger.info(f"SVG保存用ディレクトリを作成しました: {svg_dir}")

        html_content = self._acquire_content(input_html_path)
        if html_content:
            html_content, mermaid_blocks = self._extract_mermaid_blocks(html_content)
            if mermaid_blocks:
                logger.info(f"抽出されたMermaidブロック: {len(mermaid_blocks)}")
                enhanced_html = self._convert_mermaid_to_svg(html_content, mermaid_blocks, svg_dir, input_html_path)
                self._materialize_fusion(output_html_path, enhanced_html)
                logger.success("Mermaid to SVG変換プロセスが見事に完了しました")
            else:
                logger.error("Mermaidのブロックが見つからず、変換プロセスを中断します")
        else:
            logger.error("HTMLファイルの取得に失敗し、変換プロセスを中断します")

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

    def _extract_mermaid_blocks(self, html_content):
        logger.info("HTMLからMermaidブロックを抽出します")
        pattern = r'<div class="mermaid">\s*(.*?)\s*</div>'
        mermaid_blocks = []
        
        def replace_with_placeholder(match):
            placeholder = f"__MERMAID_{len(mermaid_blocks):03d}__"
            mermaid_blocks.append(match.group(1))
            return placeholder

        modified_html = re.sub(pattern, replace_with_placeholder, html_content, flags=re.DOTALL)
        
        if mermaid_blocks:
            logger.success(f"Mermaidブロックの抽出に成功しました: {len(mermaid_blocks)}個")
        else:
            logger.warning("Mermaidブロックが見つかりませんでした")
        
        return modified_html, mermaid_blocks

    def _convert_mermaid_to_svg(self, html_content, mermaid_blocks, svg_dir, input_html_path):
        logger.info("MermaidをSVGに変換します")
        current_dir = os.getcwd()
        logger.debug(f"現在の作業ディレクトリ: {current_dir}")
        
        for index, block in enumerate(mermaid_blocks):
            decoded_block = html.unescape(block)
            
            # 「-->」を「-.->」に置換
            decoded_block = decoded_block.replace('-->', '-.->')
            decoded_block = decoded_block.replace('graph TD', 'graph LR')
            
            mermaid_file = os.path.join(svg_dir, f"mermaid_{uuid.uuid4().hex}.mmd")
            svg_file = os.path.join(svg_dir, f"mermaid_{uuid.uuid4().hex}.svg")
            
            with open(mermaid_file, 'w', encoding='utf-8') as f:
                f.write(decoded_block)
                
            logger.debug(f"mermaid_file: {mermaid_file}")
            logger.debug(f"decoded block: \n{decoded_block}")
            
            cmd = [self.mmdc_path, '-i', mermaid_file, '-o', svg_file]
            
            # CSSファイルが指定されている場合、コマンドに追加
            if self.css_file:
                cmd.extend(['--cssFile', self.css_file])
            
            cmd_debug = " ".join(cmd)
            logger.debug(f"mermaid-cliを実行します: {cmd_debug}")
            try:
                result = subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=current_dir)
                logger.debug(f"mermaid-cli output: {result.stdout}")
                logger.debug(f"mermaid-cli error: {result.stderr}")
            except subprocess.CalledProcessError as e:
                logger.error(f"mermaid-cliの実行中にエラーが発生しました: {str(e)}")
                logger.error(f"mermaid-cli error output: {e.stderr}")
                continue
            
            relative_svg_path = os.path.relpath(svg_file, os.path.dirname(input_html_path)).replace('\\', '/')
            svg_tag = f'<img src="{relative_svg_path}" alt="Mermaid diagram" />'
            
            placeholder = f"__MERMAID_{index:03d}__"
            html_content = html_content.replace(placeholder, svg_tag)
            
            logger.success(f"Mermaid図 {index + 1} をSVGに変換しました: {os.path.basename(svg_file)}")

        return html_content

    def _materialize_fusion(self, file_path, content):
        logger.info(f"変換結果を{file_path}に具現化します")
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            logger.success(f"変換結果の具現化が完了しました: {file_path}")
        except Exception as e:
            logger.error(f"変換結果の具現化中に障害が発生しました: {str(e)}")

def main():
    logger.info("Mermaid to SVG変換の儀式を開始します")
    css_file = 'css/flowchart1.css'  # CSSファイルのパスを指定
    svg_converter = MermaidSVGConverter(css_file=css_file)
    svg_converter.convert_html_mermaid_to_svg(
        'example2/hovercraft_assets/enchant_codeblock.html',
        'example2/hovercraft_assets/index_with_svg.html'
    )

if __name__ == "__main__":
    main()
