from idi_model.workflow_process.monthly_projected_at_policy_level import (
    monthly_projected_policy_level,
)

from idi_model.workflow_process.quarterly_projected_at_policy_level import (
    quarterly_projected_policy_level,
)

from idi_model.workflow_process.quarterly_projected_at_cohort_level import (
    quarterly_projected_cohort_level,
)
from idi_model.abstracted_packages import furtheredge_pandas as pd
from idi_model.workflow_process.concat_data import concat_all_dfs, split_data


def full_idi_workflow(
    deposit_df: pd.DataFrame,
    activation_df: pd.DataFrame,
    cohort_df: pd.DataFrame,
    monthly_loss_ratio_df: pd.DataFrame,
    config: dict,
    chunk_size=1000,
):
    deposit_df["activation_status"] = False
    activation_df["activation_status"] = True

    combined_deposit_activation_df = concat_all_dfs(
        activation_df,
        deposit_df,
        config["keys_df_mapping_deposit"],
        config["keys_df_mapping_activation"],
        None,
    )

    deposit_data, activation_data = split_data(
        combined_deposit_activation_df,
        config["run_settings"]["reporting_date"],
        config["run_settings"]["next_reporting_date"],
    )

    df_monthly_policy_level, df_monthly_policy_level_not_projected = (
        monthly_projected_policy_level(
            deposit_data,
            cohort_df,
            monthly_loss_ratio_df,
            config["list_projected_columns"],
            config["list_non_projected_columns"],
            config["pivot_variables"],
            config["agg_variables"],
            config["columns_keep_df_deposit"],
            config["values_policy_status"],
            config["run_settings"],
            "deposit",
            chunk_size=chunk_size,
            return_projected_df=True,
            return_non_projected_df=True,
            write_projected_to_csv=False,
            write_non_projected_to_csv=False,
            projected_csv_path=None,
            non_projected_csv_path=None,
        )
    )

    (
        df_monthly_policy_level_activation,
        df_monthly_policy_level_not_projected_activation,
    ) = monthly_projected_policy_level(
        activation_data,
        cohort_df,
        monthly_loss_ratio_df,
        config["list_projected_columns"],
        config["list_non_projected_columns"],
        config["pivot_variables"],
        config["agg_variables"],
        config["columns_keep_df_activation"],
        config["values_policy_status"],
        config["run_settings"],
        "activation",
        chunk_size=chunk_size,
        return_projected_df=True,
        return_non_projected_df=True,
        write_projected_to_csv=False,
        write_non_projected_to_csv=False,
        projected_csv_path=None,
        non_projected_csv_path=None,
    )

    df_monthly_policy_level = pd.concat(
        [
            df_monthly_policy_level,
            df_monthly_policy_level_activation,
        ],
        ignore_index=True,
    )

    df_monthly_policy_level_not_projected = pd.concat(
        [
            df_monthly_policy_level_not_projected,
            df_monthly_policy_level_not_projected_activation,
        ],
        ignore_index=True,
    )

    list_projected_columns_final = config["list_projected_columns_final"]

    df_quarterly_policy_level = quarterly_projected_policy_level(
        df_monthly_policy_level, list_projected_columns_final
    )

    df_quarterly_cohort_level = quarterly_projected_cohort_level(
        df_monthly_policy_level, list_projected_columns_final
    )

    return (
        df_monthly_policy_level,
        df_monthly_policy_level_not_projected,
        df_quarterly_policy_level,
        df_quarterly_cohort_level,
    )


def ifrs17_compliant_before_activation(
    deposit_data_before_activation,
    activation_data_before_activation,
    cohort_parameters_data,
    monthly_loss_ratio_df,
    config,
):
    activation_data_before_activation["activation_status"] = False
    deposit_data_before_activation["activation_status"] = False
    deposit_data_before_activation = pd.concat(
        [deposit_data_before_activation, activation_data_before_activation]
    )
    deposit_data_before_activation.reset_index(drop=True, inplace=True)
    (
        df_monthly_policy_level_projected,
        df_monthly_policy_level_not_projected,
    ) = monthly_projected_policy_level(
        deposit_data_before_activation,
        cohort_parameters_data,
        monthly_loss_ratio_df,
        config["list_projected_columns"],
        config["list_non_projected_columns"],
        config["pivot_variables"],
        config["agg_variables"],
        config["columns_keep_df_deposit"],
        config["values_policy_status"],
        config["run_settings"],
        "deposit",
        chunk_size=1000,
        return_projected_df=True,
        return_non_projected_df=True,
        write_projected_to_csv=False,
        write_non_projected_to_csv=False,
        projected_csv_path=None,
        non_projected_csv_path=None,
    )
    df_quarterly_cohort_level = quarterly_projected_cohort_level(
        df_monthly_policy_level_projected,
        config["list_projected_columns_final"],
    )
    return df_quarterly_cohort_level, df_monthly_policy_level_not_projected


def ifrs17_compliant_after_activation(
    deposit_df,
    activation_df,
    cohort_df,
    monthly_loss_ratio_df,
    config,
    chunk_size=1000,
):
    deposit_df["activation_status"] = False
    activation_df["activation_status"] = True

    df_monthly_policy_level, df_monthly_policy_level_not_projected = (
        monthly_projected_policy_level(
            deposit_df,
            cohort_df,
            monthly_loss_ratio_df,
            config["list_projected_columns"],
            config["list_non_projected_columns"],
            config["pivot_variables"],
            config["agg_variables"],
            config["columns_keep_df_deposit"],
            config["values_policy_status"],
            config["run_settings"],
            "deposit",
            chunk_size=chunk_size,
            return_projected_df=True,
            return_non_projected_df=True,
            write_projected_to_csv=False,
            write_non_projected_to_csv=False,
            projected_csv_path=None,
            non_projected_csv_path=None,
        )
    )

    (
        df_monthly_policy_level_activation,
        df_monthly_policy_level_not_projected_activation,
    ) = monthly_projected_policy_level(
        activation_df,
        cohort_df,
        monthly_loss_ratio_df,
        config["list_projected_columns"],
        config["list_non_projected_columns"],
        config["pivot_variables"],
        config["agg_variables"],
        config["columns_keep_df_activation"],
        config["values_policy_status"],
        config["run_settings"],
        "activation",
        chunk_size=chunk_size,
        return_projected_df=True,
        return_non_projected_df=True,
        write_projected_to_csv=False,
        write_non_projected_to_csv=False,
        projected_csv_path=None,
        non_projected_csv_path=None,
    )

    df_monthly_policy_level = pd.concat(
        [
            df_monthly_policy_level,
            df_monthly_policy_level_activation,
        ],
        ignore_index=True,
    )

    df_monthly_policy_level_not_projected = pd.concat(
        [
            df_monthly_policy_level_not_projected,
            df_monthly_policy_level_not_projected_activation,
        ],
        ignore_index=True,
    )

    list_projected_columns_final = config["list_projected_columns_final"]

    df_quarterly_cohort_level = quarterly_projected_cohort_level(
        df_monthly_policy_level, list_projected_columns_final
    )

    return (
        df_quarterly_cohort_level,
        df_monthly_policy_level_not_projected,
    )


def convert_to_ifrs17_compliant(
    deposit_df: pd.DataFrame,
    activation_df: pd.DataFrame,
    cohort_df: pd.DataFrame,
    monthly_loss_ratio_df: pd.DataFrame,
    config: dict,
    chunk_size=1000,
):

    deposit_df["activation_status"] = False
    activation_df["activation_status"] = True

    combined_deposit_activation_df = concat_all_dfs(
        activation_df,
        deposit_df,
        config["keys_df_mapping_deposit"],
        config["keys_df_mapping_activation"],
        None,
    )

    deposit_data, activation_data = split_data(
        combined_deposit_activation_df,
        config["run_settings"]["reporting_date"],
        config["run_settings"]["next_reporting_date"],
    )
    deposit_data = deposit_data[:50]
    activation_data = activation_data[:50]

    deposit_data_before_activation = deposit_data.copy(deep=True)
    activation_data_before_activation = activation_data.copy(deep=True)
    (
        df_quarterly_cohort_level_before_activation,
        df_monthly_policy_level_not_projected_before_activation,
    ) = ifrs17_compliant_before_activation(
        deposit_data_before_activation,
        activation_data_before_activation,
        cohort_df,
        monthly_loss_ratio_df,
        config,
    )
    df_quarterly_cohort_level_before_activation["ProjectionType"] = (
        "Before Activation"
    )
    print("start run afteractivation")
    (
        df_quarterly_cohort_level_after_activation,
        df_monthly_policy_level_not_projected_after_activation,
    ) = ifrs17_compliant_after_activation(
        deposit_df,
        activation_df,
        cohort_df,
        monthly_loss_ratio_df,
        config,
        chunk_size=1000,
    )
    df_quarterly_cohort_level_after_activation["ProjectionType"] = (
        "After Activation"
    )
    df_irfs17_input_result = pd.concat(
        [
            df_quarterly_cohort_level_before_activation,
            df_quarterly_cohort_level_after_activation,
        ]
    )
    return (
        df_irfs17_input_result,
        df_monthly_policy_level_not_projected_after_activation,
        df_monthly_policy_level_not_projected_before_activation,
    )
