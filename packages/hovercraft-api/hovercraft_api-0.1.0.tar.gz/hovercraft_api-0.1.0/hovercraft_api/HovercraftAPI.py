import os
from loguru import logger
import shutil

from .markdown_to_rst_converter import MarkdownToRSTConverter
from .rst_adjuster import RSTAdjuster
from .hovercraft_converter import HovercraftConverter
from .mermaid_alchemist import MermaidFusionMaster
from .code_block_alchemist import CodeBlockTransmuter
from .markdown_to_slides_converter import MarkdownToSlidesConverter
from art import *

class HovercraftAPI:
    def __init__(self, markdown_file, css_file='css/mytheme.css'):
        self.markdown_file = markdown_file
        self.working_dir = os.getcwd()
        self.markdown_dir = os.path.dirname(self.markdown_file)
        self.css_file = css_file
        self.assets_dir = os.path.join(self.markdown_dir, 'hovercraft_assets')
        self.slides_md_file = os.path.join(self.assets_dir, 'slides.md')
        self.rst_file = os.path.join(self.assets_dir, 'temp.rst')
        self.hovercraft_rst_file = os.path.join(self.assets_dir, 'temp_hovercraft.rst')
        self.html_file = os.path.join(self.assets_dir, 'index.html')
        self.mermaid_html_file = os.path.join(self.assets_dir, 'enchant_mermaid.html')
        self.codeblock_html_file = os.path.join(self.assets_dir, 'enchant_codeblock.html')

        # CSSファイルのパスを設定
        self.css_src = os.path.join(self.working_dir, self.css_file)
        self.css_dest = os.path.join(self.assets_dir, self.css_file)

        # 各コンバーターのインスタンスを作成
        self.md_to_rst_converter = MarkdownToRSTConverter()
        self.rst_adjuster = RSTAdjuster(css_file=self.css_file)
        self.hovercraft_converter = HovercraftConverter(output_dir=self.assets_dir, css_file=self.css_file)
        self.mermaid_fusion_master = MermaidFusionMaster()
        self.codeblock_transmuter = CodeBlockTransmuter()
        self.md_to_slides_converter = MarkdownToSlidesConverter()

        os.makedirs(self.assets_dir, exist_ok=True)
        self._copy_assets()
        logger.info("HovercraftAPI initialized")

    def _copy_assets(self):
        """CSSファイルなどのアセットを適切なディレクトリにコピーする"""
        if os.path.exists(self.css_src):
            os.makedirs(os.path.dirname(self.css_dest), exist_ok=True)
            shutil.copy2(self.css_src, self.css_dest)
            logger.info(f"Copied CSS file from {self.css_src} to {self.css_dest}")
        else:
            logger.warning(f"CSS file not found at {self.css_src}")

    def generate_slides(self):
        """MarkdownファイルからHovercraftスライドを生成する"""
        try:
            # スライド用マークダウンファイルを生成
            self.md_to_slides_converter.convert_file(self.markdown_file, self.slides_md_file)

            # MarkdownをRSTに変換
            self.md_to_rst_converter.convert(self.slides_md_file, self.rst_file)

            # RSTをHovercraft用に調整
            self.rst_adjuster.adjust_for_hovercraft(self.rst_file, self.hovercraft_rst_file)

            # Hovercraftを実行してHTMLスライドを生成
            self.hovercraft_converter.convert(self.hovercraft_rst_file)

            # Mermaidを統合
            self.mermaid_fusion_master.orchestrate_fusion(self.html_file, self.slides_md_file, self.mermaid_html_file)

            # コードブロック変換を実行
            self.codeblock_transmuter.transmute_documents(self.mermaid_html_file, self.slides_md_file, self.codeblock_html_file)

            logger.success(f"Hovercraftスライド生成が完了しました: {self.html_file}")
            return True

        except Exception as e:
            logger.error(f"スライド生成中にエラーが発生しました: {str(e)}")
            return False
        
def cli():
    import argparse
    print(tprint("  HovercraftAPI",font="rnd-large"))
    parser = argparse.ArgumentParser(
        description="MarkdownからHovercraftスライドを生成します", 
        prog='hovercraftapi'
    )
    parser.add_argument("markdown_file", help="入力Markdownファイル")
    parser.add_argument("-c", "--css", default="css/mytheme.css", help="CSSファイル（作業ディレクトリからの相対パス）")

    args = parser.parse_args()

    api = HovercraftAPI(args.markdown_file, css_file=args.css)
    api.generate_slides()

if __name__ == "__main__":
    cli()
