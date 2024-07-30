# hovercraft_api/HovercraftAPI.py
import os
from loguru import logger
import shutil
import argparse

from .markdown_to_rst_converter import MarkdownToRSTConverter
from .rst_adjuster import RSTAdjuster
from .hovercraft_converter import HovercraftConverter
from .mermaid_alchemist import MermaidFusionMaster
from .code_block_alchemist import CodeBlockTransmuter
from .markdown_to_slides_converter import MarkdownToSlidesConverter
from .dynamic_rst_adjuster import DynamicRSTAdjuster
from .mermaid_svg_converter import MermaidSVGConverter
from art import *

class HovercraftAPI:
    def __init__(self, markdown_file, css_file='css/mytheme.css', 
                 grid_width=6000, grid_height=6000, grid_depth=6000, 
                 slide_width=1000, slide_height=750, slide_depth=1000,
                 enable_dynamic_position=True, 
                 use_rotate_x=False, use_rotate_y=False, use_rotate_z=False):

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

        # DynamicRSTAdjuster のインスタンスを作成
        self.dynamic_rst_adjuster = DynamicRSTAdjuster(
            grid_width=grid_width,
            grid_height=grid_height,
            grid_depth=grid_depth,
            slide_width=slide_width,
            slide_height=slide_height,
            slide_depth=slide_depth,
            css_file=self.css_file,
            use_rotate_x=use_rotate_x,
            use_rotate_y=use_rotate_y,
            use_rotate_z=use_rotate_z
        )
        self.enable_dynamic_position = enable_dynamic_position
        os.makedirs(self.assets_dir, exist_ok=True)
        self._copy_assets()
        
        self.mermaid_svg_converter = MermaidSVGConverter(css_file=self.css_file)
        self.svg_html_file = os.path.join(self.assets_dir, 'index_with_svg.html')
        
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

            # enable_dynamic_position が True の場合のみ DynamicRSTAdjuster を実行
            if self.enable_dynamic_position:
                # DynamicRSTAdjuster 用の出力ファイル名を設定
                dynamic_hovercraft_rst_file = os.path.join(self.assets_dir, 'temp_dynamic_hovercraft.rst')  
                self.dynamic_rst_adjuster.adjust_for_dynamic_hovercraft(self.hovercraft_rst_file, dynamic_hovercraft_rst_file)

                # 後の工程で使用するファイル名を更新
                self.hovercraft_rst_file = dynamic_hovercraft_rst_file 

            # Hovercraftを実行してHTMLスライドを生成
            self.hovercraft_converter.convert(self.hovercraft_rst_file)

            # Mermaidを統合
            self.mermaid_fusion_master.orchestrate_fusion(self.html_file, self.mermaid_html_file)
            
            # コードブロック変換を実行
            self.codeblock_transmuter.transmute_documents(self.mermaid_html_file, self.slides_md_file, self.codeblock_html_file)

            # MermaidをSVGに変換
            self.mermaid_svg_converter.convert_html_mermaid_to_svg(self.codeblock_html_file, self.svg_html_file)

            logger.success(f"Hovercraftスライド生成が完了しました: {self.svg_html_file}")
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

    # DynamicRSTAdjuster のパラメータ
    parser.add_argument("--grid-width", type=int, default=6000, help="グリッドの幅")
    parser.add_argument("--grid-height", type=int, default=6000, help="グリッドの高さ")
    parser.add_argument("--grid-depth", type=int, default=6000, help="グリッドの奥行き")
    parser.add_argument("--slide-width", type=int, default=1000, help="スライドの幅")
    parser.add_argument("--slide-height", type=int, default=750, help="スライドの高さ")
    parser.add_argument("--slide-depth", type=int, default=1000, help="スライドの奥行き")
    parser.add_argument("--enable-dynamic-position", action="store_true", help="動的なスライド位置を有効にする")
    parser.add_argument("--use-rotate-x", action="store_true", help="X軸回転を有効にする")
    parser.add_argument("--use-rotate-y", action="store_true", help="Y軸回転を有効にする")
    parser.add_argument("--use-rotate-z", action="store_true", help="Z軸回転を有効にする")

    args = parser.parse_args()

    api = HovercraftAPI(
        args.markdown_file, 
        css_file=args.css,
        grid_width=args.grid_width,
        grid_height=args.grid_height,
        grid_depth=args.grid_depth,
        slide_width=args.slide_width,
        slide_height=args.slide_height,
        slide_depth=args.slide_depth,
        enable_dynamic_position=args.enable_dynamic_position,
        use_rotate_x=args.use_rotate_x,
        use_rotate_y=args.use_rotate_y,
        use_rotate_z=args.use_rotate_z
    )
    api.generate_slides()

if __name__ == "__main__":
    cli()
