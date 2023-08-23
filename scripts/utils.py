def sort_and_filter(p_df,p_col,p_start,p_end):
    # sort by column 
    p_df = p_df.sort_values(by=[p_col])
    # filter to between start and end 
    p_df = p_df[(p_df[p_col] > p_start)]
    p_df = p_df[(p_df[p_col] <= p_end)]
    return(p_df)

