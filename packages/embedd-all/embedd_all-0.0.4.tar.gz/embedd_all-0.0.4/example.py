from src.embed_all.index import modify_excel_for_embedding

if __name__ == '__main__':
    # Example usage
    file_path = '/Users/arnabbhattachargya/Desktop/data.xlsx'
    context = "data"
    dfs = modify_excel_for_embedding(file_path=file_path, context=context)
    print(dfs[2].head(3))