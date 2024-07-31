from src.embedd_all.index import modify_excel_for_embedding, process_pdf

if __name__ == '__main__':
    # Example usage
    file_path = '/Users/arnabbhattachargya/Desktop/data.xlsx'
    file_path = '/Users/arnabbhattachargya/Desktop/setu-product/UMAP.pdf'
    context = "data"
    # dfs = modify_excel_for_embedding(file_path=file_path, context=context)
    # print(dfs[2].head(3))

    texts = process_pdf(file_path)
    print("Text Length: ", len(texts))
    print("Text process: ", texts)