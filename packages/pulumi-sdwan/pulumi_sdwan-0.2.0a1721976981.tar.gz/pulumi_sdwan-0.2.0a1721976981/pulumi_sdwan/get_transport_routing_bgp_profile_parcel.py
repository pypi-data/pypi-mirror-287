# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetTransportRoutingBgpProfileParcelResult',
    'AwaitableGetTransportRoutingBgpProfileParcelResult',
    'get_transport_routing_bgp_profile_parcel',
    'get_transport_routing_bgp_profile_parcel_output',
]

@pulumi.output_type
class GetTransportRoutingBgpProfileParcelResult:
    """
    A collection of values returned by getTransportRoutingBgpProfileParcel.
    """
    def __init__(__self__, always_compare_med=None, always_compare_med_variable=None, as_number=None, as_number_variable=None, compare_router_id=None, compare_router_id_variable=None, description=None, deterministic_med=None, deterministic_med_variable=None, external_routes_distance=None, external_routes_distance_variable=None, feature_profile_id=None, hold_time=None, hold_time_variable=None, id=None, internal_routes_distance=None, internal_routes_distance_variable=None, ipv4_aggregate_addresses=None, ipv4_eibgp_maximum_paths=None, ipv4_eibgp_maximum_paths_variable=None, ipv4_neighbors=None, ipv4_networks=None, ipv4_originate=None, ipv4_originate_variable=None, ipv4_redistributes=None, ipv4_table_map_filter=None, ipv4_table_map_filter_variable=None, ipv4_table_map_route_policy_id=None, ipv6_aggregate_addresses=None, ipv6_eibgp_maximum_paths=None, ipv6_eibgp_maximum_paths_variable=None, ipv6_neighbors=None, ipv6_networks=None, ipv6_originate=None, ipv6_originate_variable=None, ipv6_redistributes=None, ipv6_table_map_filter=None, ipv6_table_map_filter_variable=None, ipv6_table_map_route_policy_id=None, keepalive_time=None, keepalive_time_variable=None, local_routes_distance=None, local_routes_distance_variable=None, missing_med_as_worst=None, missing_med_as_worst_variable=None, mpls_interfaces=None, multipath_relax=None, multipath_relax_variable=None, name=None, propagate_as_path=None, propagate_as_path_variable=None, propagate_community=None, propagate_community_variable=None, router_id=None, router_id_variable=None, version=None):
        if always_compare_med and not isinstance(always_compare_med, bool):
            raise TypeError("Expected argument 'always_compare_med' to be a bool")
        pulumi.set(__self__, "always_compare_med", always_compare_med)
        if always_compare_med_variable and not isinstance(always_compare_med_variable, str):
            raise TypeError("Expected argument 'always_compare_med_variable' to be a str")
        pulumi.set(__self__, "always_compare_med_variable", always_compare_med_variable)
        if as_number and not isinstance(as_number, int):
            raise TypeError("Expected argument 'as_number' to be a int")
        pulumi.set(__self__, "as_number", as_number)
        if as_number_variable and not isinstance(as_number_variable, str):
            raise TypeError("Expected argument 'as_number_variable' to be a str")
        pulumi.set(__self__, "as_number_variable", as_number_variable)
        if compare_router_id and not isinstance(compare_router_id, bool):
            raise TypeError("Expected argument 'compare_router_id' to be a bool")
        pulumi.set(__self__, "compare_router_id", compare_router_id)
        if compare_router_id_variable and not isinstance(compare_router_id_variable, str):
            raise TypeError("Expected argument 'compare_router_id_variable' to be a str")
        pulumi.set(__self__, "compare_router_id_variable", compare_router_id_variable)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if deterministic_med and not isinstance(deterministic_med, bool):
            raise TypeError("Expected argument 'deterministic_med' to be a bool")
        pulumi.set(__self__, "deterministic_med", deterministic_med)
        if deterministic_med_variable and not isinstance(deterministic_med_variable, str):
            raise TypeError("Expected argument 'deterministic_med_variable' to be a str")
        pulumi.set(__self__, "deterministic_med_variable", deterministic_med_variable)
        if external_routes_distance and not isinstance(external_routes_distance, int):
            raise TypeError("Expected argument 'external_routes_distance' to be a int")
        pulumi.set(__self__, "external_routes_distance", external_routes_distance)
        if external_routes_distance_variable and not isinstance(external_routes_distance_variable, str):
            raise TypeError("Expected argument 'external_routes_distance_variable' to be a str")
        pulumi.set(__self__, "external_routes_distance_variable", external_routes_distance_variable)
        if feature_profile_id and not isinstance(feature_profile_id, str):
            raise TypeError("Expected argument 'feature_profile_id' to be a str")
        pulumi.set(__self__, "feature_profile_id", feature_profile_id)
        if hold_time and not isinstance(hold_time, int):
            raise TypeError("Expected argument 'hold_time' to be a int")
        pulumi.set(__self__, "hold_time", hold_time)
        if hold_time_variable and not isinstance(hold_time_variable, str):
            raise TypeError("Expected argument 'hold_time_variable' to be a str")
        pulumi.set(__self__, "hold_time_variable", hold_time_variable)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_routes_distance and not isinstance(internal_routes_distance, int):
            raise TypeError("Expected argument 'internal_routes_distance' to be a int")
        pulumi.set(__self__, "internal_routes_distance", internal_routes_distance)
        if internal_routes_distance_variable and not isinstance(internal_routes_distance_variable, str):
            raise TypeError("Expected argument 'internal_routes_distance_variable' to be a str")
        pulumi.set(__self__, "internal_routes_distance_variable", internal_routes_distance_variable)
        if ipv4_aggregate_addresses and not isinstance(ipv4_aggregate_addresses, list):
            raise TypeError("Expected argument 'ipv4_aggregate_addresses' to be a list")
        pulumi.set(__self__, "ipv4_aggregate_addresses", ipv4_aggregate_addresses)
        if ipv4_eibgp_maximum_paths and not isinstance(ipv4_eibgp_maximum_paths, int):
            raise TypeError("Expected argument 'ipv4_eibgp_maximum_paths' to be a int")
        pulumi.set(__self__, "ipv4_eibgp_maximum_paths", ipv4_eibgp_maximum_paths)
        if ipv4_eibgp_maximum_paths_variable and not isinstance(ipv4_eibgp_maximum_paths_variable, str):
            raise TypeError("Expected argument 'ipv4_eibgp_maximum_paths_variable' to be a str")
        pulumi.set(__self__, "ipv4_eibgp_maximum_paths_variable", ipv4_eibgp_maximum_paths_variable)
        if ipv4_neighbors and not isinstance(ipv4_neighbors, list):
            raise TypeError("Expected argument 'ipv4_neighbors' to be a list")
        pulumi.set(__self__, "ipv4_neighbors", ipv4_neighbors)
        if ipv4_networks and not isinstance(ipv4_networks, list):
            raise TypeError("Expected argument 'ipv4_networks' to be a list")
        pulumi.set(__self__, "ipv4_networks", ipv4_networks)
        if ipv4_originate and not isinstance(ipv4_originate, bool):
            raise TypeError("Expected argument 'ipv4_originate' to be a bool")
        pulumi.set(__self__, "ipv4_originate", ipv4_originate)
        if ipv4_originate_variable and not isinstance(ipv4_originate_variable, str):
            raise TypeError("Expected argument 'ipv4_originate_variable' to be a str")
        pulumi.set(__self__, "ipv4_originate_variable", ipv4_originate_variable)
        if ipv4_redistributes and not isinstance(ipv4_redistributes, list):
            raise TypeError("Expected argument 'ipv4_redistributes' to be a list")
        pulumi.set(__self__, "ipv4_redistributes", ipv4_redistributes)
        if ipv4_table_map_filter and not isinstance(ipv4_table_map_filter, bool):
            raise TypeError("Expected argument 'ipv4_table_map_filter' to be a bool")
        pulumi.set(__self__, "ipv4_table_map_filter", ipv4_table_map_filter)
        if ipv4_table_map_filter_variable and not isinstance(ipv4_table_map_filter_variable, str):
            raise TypeError("Expected argument 'ipv4_table_map_filter_variable' to be a str")
        pulumi.set(__self__, "ipv4_table_map_filter_variable", ipv4_table_map_filter_variable)
        if ipv4_table_map_route_policy_id and not isinstance(ipv4_table_map_route_policy_id, str):
            raise TypeError("Expected argument 'ipv4_table_map_route_policy_id' to be a str")
        pulumi.set(__self__, "ipv4_table_map_route_policy_id", ipv4_table_map_route_policy_id)
        if ipv6_aggregate_addresses and not isinstance(ipv6_aggregate_addresses, list):
            raise TypeError("Expected argument 'ipv6_aggregate_addresses' to be a list")
        pulumi.set(__self__, "ipv6_aggregate_addresses", ipv6_aggregate_addresses)
        if ipv6_eibgp_maximum_paths and not isinstance(ipv6_eibgp_maximum_paths, int):
            raise TypeError("Expected argument 'ipv6_eibgp_maximum_paths' to be a int")
        pulumi.set(__self__, "ipv6_eibgp_maximum_paths", ipv6_eibgp_maximum_paths)
        if ipv6_eibgp_maximum_paths_variable and not isinstance(ipv6_eibgp_maximum_paths_variable, str):
            raise TypeError("Expected argument 'ipv6_eibgp_maximum_paths_variable' to be a str")
        pulumi.set(__self__, "ipv6_eibgp_maximum_paths_variable", ipv6_eibgp_maximum_paths_variable)
        if ipv6_neighbors and not isinstance(ipv6_neighbors, list):
            raise TypeError("Expected argument 'ipv6_neighbors' to be a list")
        pulumi.set(__self__, "ipv6_neighbors", ipv6_neighbors)
        if ipv6_networks and not isinstance(ipv6_networks, list):
            raise TypeError("Expected argument 'ipv6_networks' to be a list")
        pulumi.set(__self__, "ipv6_networks", ipv6_networks)
        if ipv6_originate and not isinstance(ipv6_originate, bool):
            raise TypeError("Expected argument 'ipv6_originate' to be a bool")
        pulumi.set(__self__, "ipv6_originate", ipv6_originate)
        if ipv6_originate_variable and not isinstance(ipv6_originate_variable, str):
            raise TypeError("Expected argument 'ipv6_originate_variable' to be a str")
        pulumi.set(__self__, "ipv6_originate_variable", ipv6_originate_variable)
        if ipv6_redistributes and not isinstance(ipv6_redistributes, list):
            raise TypeError("Expected argument 'ipv6_redistributes' to be a list")
        pulumi.set(__self__, "ipv6_redistributes", ipv6_redistributes)
        if ipv6_table_map_filter and not isinstance(ipv6_table_map_filter, bool):
            raise TypeError("Expected argument 'ipv6_table_map_filter' to be a bool")
        pulumi.set(__self__, "ipv6_table_map_filter", ipv6_table_map_filter)
        if ipv6_table_map_filter_variable and not isinstance(ipv6_table_map_filter_variable, str):
            raise TypeError("Expected argument 'ipv6_table_map_filter_variable' to be a str")
        pulumi.set(__self__, "ipv6_table_map_filter_variable", ipv6_table_map_filter_variable)
        if ipv6_table_map_route_policy_id and not isinstance(ipv6_table_map_route_policy_id, str):
            raise TypeError("Expected argument 'ipv6_table_map_route_policy_id' to be a str")
        pulumi.set(__self__, "ipv6_table_map_route_policy_id", ipv6_table_map_route_policy_id)
        if keepalive_time and not isinstance(keepalive_time, int):
            raise TypeError("Expected argument 'keepalive_time' to be a int")
        pulumi.set(__self__, "keepalive_time", keepalive_time)
        if keepalive_time_variable and not isinstance(keepalive_time_variable, str):
            raise TypeError("Expected argument 'keepalive_time_variable' to be a str")
        pulumi.set(__self__, "keepalive_time_variable", keepalive_time_variable)
        if local_routes_distance and not isinstance(local_routes_distance, int):
            raise TypeError("Expected argument 'local_routes_distance' to be a int")
        pulumi.set(__self__, "local_routes_distance", local_routes_distance)
        if local_routes_distance_variable and not isinstance(local_routes_distance_variable, str):
            raise TypeError("Expected argument 'local_routes_distance_variable' to be a str")
        pulumi.set(__self__, "local_routes_distance_variable", local_routes_distance_variable)
        if missing_med_as_worst and not isinstance(missing_med_as_worst, bool):
            raise TypeError("Expected argument 'missing_med_as_worst' to be a bool")
        pulumi.set(__self__, "missing_med_as_worst", missing_med_as_worst)
        if missing_med_as_worst_variable and not isinstance(missing_med_as_worst_variable, str):
            raise TypeError("Expected argument 'missing_med_as_worst_variable' to be a str")
        pulumi.set(__self__, "missing_med_as_worst_variable", missing_med_as_worst_variable)
        if mpls_interfaces and not isinstance(mpls_interfaces, list):
            raise TypeError("Expected argument 'mpls_interfaces' to be a list")
        pulumi.set(__self__, "mpls_interfaces", mpls_interfaces)
        if multipath_relax and not isinstance(multipath_relax, bool):
            raise TypeError("Expected argument 'multipath_relax' to be a bool")
        pulumi.set(__self__, "multipath_relax", multipath_relax)
        if multipath_relax_variable and not isinstance(multipath_relax_variable, str):
            raise TypeError("Expected argument 'multipath_relax_variable' to be a str")
        pulumi.set(__self__, "multipath_relax_variable", multipath_relax_variable)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if propagate_as_path and not isinstance(propagate_as_path, bool):
            raise TypeError("Expected argument 'propagate_as_path' to be a bool")
        pulumi.set(__self__, "propagate_as_path", propagate_as_path)
        if propagate_as_path_variable and not isinstance(propagate_as_path_variable, str):
            raise TypeError("Expected argument 'propagate_as_path_variable' to be a str")
        pulumi.set(__self__, "propagate_as_path_variable", propagate_as_path_variable)
        if propagate_community and not isinstance(propagate_community, bool):
            raise TypeError("Expected argument 'propagate_community' to be a bool")
        pulumi.set(__self__, "propagate_community", propagate_community)
        if propagate_community_variable and not isinstance(propagate_community_variable, str):
            raise TypeError("Expected argument 'propagate_community_variable' to be a str")
        pulumi.set(__self__, "propagate_community_variable", propagate_community_variable)
        if router_id and not isinstance(router_id, str):
            raise TypeError("Expected argument 'router_id' to be a str")
        pulumi.set(__self__, "router_id", router_id)
        if router_id_variable and not isinstance(router_id_variable, str):
            raise TypeError("Expected argument 'router_id_variable' to be a str")
        pulumi.set(__self__, "router_id_variable", router_id_variable)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="alwaysCompareMed")
    def always_compare_med(self) -> bool:
        """
        Compare MEDs from all ASs when selecting active BGP paths
        """
        return pulumi.get(self, "always_compare_med")

    @property
    @pulumi.getter(name="alwaysCompareMedVariable")
    def always_compare_med_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "always_compare_med_variable")

    @property
    @pulumi.getter(name="asNumber")
    def as_number(self) -> int:
        """
        Set autonomous system number \\n\\n or \\n\\n
        """
        return pulumi.get(self, "as_number")

    @property
    @pulumi.getter(name="asNumberVariable")
    def as_number_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "as_number_variable")

    @property
    @pulumi.getter(name="compareRouterId")
    def compare_router_id(self) -> bool:
        """
        Compare router IDs when selecting active BGP paths
        """
        return pulumi.get(self, "compare_router_id")

    @property
    @pulumi.getter(name="compareRouterIdVariable")
    def compare_router_id_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "compare_router_id_variable")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the profile parcel
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deterministicMed")
    def deterministic_med(self) -> bool:
        """
        Compare MEDs from all routes from same AS when selecting active BGP paths
        """
        return pulumi.get(self, "deterministic_med")

    @property
    @pulumi.getter(name="deterministicMedVariable")
    def deterministic_med_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "deterministic_med_variable")

    @property
    @pulumi.getter(name="externalRoutesDistance")
    def external_routes_distance(self) -> int:
        """
        Set administrative distance for external BGP routes
        """
        return pulumi.get(self, "external_routes_distance")

    @property
    @pulumi.getter(name="externalRoutesDistanceVariable")
    def external_routes_distance_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "external_routes_distance_variable")

    @property
    @pulumi.getter(name="featureProfileId")
    def feature_profile_id(self) -> str:
        """
        Feature Profile ID
        """
        return pulumi.get(self, "feature_profile_id")

    @property
    @pulumi.getter(name="holdTime")
    def hold_time(self) -> int:
        """
        Interval (seconds) not receiving a keepalive message declares a BGP peer down
        """
        return pulumi.get(self, "hold_time")

    @property
    @pulumi.getter(name="holdTimeVariable")
    def hold_time_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "hold_time_variable")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the profile parcel
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalRoutesDistance")
    def internal_routes_distance(self) -> int:
        """
        Set administrative distance for internal BGP routes
        """
        return pulumi.get(self, "internal_routes_distance")

    @property
    @pulumi.getter(name="internalRoutesDistanceVariable")
    def internal_routes_distance_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "internal_routes_distance_variable")

    @property
    @pulumi.getter(name="ipv4AggregateAddresses")
    def ipv4_aggregate_addresses(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv4AggregateAddressResult']:
        """
        Aggregate prefixes in specific range
        """
        return pulumi.get(self, "ipv4_aggregate_addresses")

    @property
    @pulumi.getter(name="ipv4EibgpMaximumPaths")
    def ipv4_eibgp_maximum_paths(self) -> int:
        """
        Set maximum number of parallel IBGP paths for multipath load sharing
        """
        return pulumi.get(self, "ipv4_eibgp_maximum_paths")

    @property
    @pulumi.getter(name="ipv4EibgpMaximumPathsVariable")
    def ipv4_eibgp_maximum_paths_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "ipv4_eibgp_maximum_paths_variable")

    @property
    @pulumi.getter(name="ipv4Neighbors")
    def ipv4_neighbors(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv4NeighborResult']:
        """
        Set BGP IPv4 neighbors
        """
        return pulumi.get(self, "ipv4_neighbors")

    @property
    @pulumi.getter(name="ipv4Networks")
    def ipv4_networks(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv4NetworkResult']:
        """
        Configure the networks for BGP to advertise
        """
        return pulumi.get(self, "ipv4_networks")

    @property
    @pulumi.getter(name="ipv4Originate")
    def ipv4_originate(self) -> bool:
        """
        BGP Default Information Originate
        """
        return pulumi.get(self, "ipv4_originate")

    @property
    @pulumi.getter(name="ipv4OriginateVariable")
    def ipv4_originate_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "ipv4_originate_variable")

    @property
    @pulumi.getter(name="ipv4Redistributes")
    def ipv4_redistributes(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv4RedistributeResult']:
        """
        Redistribute routes into BGP
        """
        return pulumi.get(self, "ipv4_redistributes")

    @property
    @pulumi.getter(name="ipv4TableMapFilter")
    def ipv4_table_map_filter(self) -> bool:
        """
        Table map filtered or not
        """
        return pulumi.get(self, "ipv4_table_map_filter")

    @property
    @pulumi.getter(name="ipv4TableMapFilterVariable")
    def ipv4_table_map_filter_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "ipv4_table_map_filter_variable")

    @property
    @pulumi.getter(name="ipv4TableMapRoutePolicyId")
    def ipv4_table_map_route_policy_id(self) -> str:
        return pulumi.get(self, "ipv4_table_map_route_policy_id")

    @property
    @pulumi.getter(name="ipv6AggregateAddresses")
    def ipv6_aggregate_addresses(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv6AggregateAddressResult']:
        """
        IPv6 Aggregate prefixes in specific range
        """
        return pulumi.get(self, "ipv6_aggregate_addresses")

    @property
    @pulumi.getter(name="ipv6EibgpMaximumPaths")
    def ipv6_eibgp_maximum_paths(self) -> int:
        """
        Set maximum number of parallel IBGP paths for multipath load sharing
        """
        return pulumi.get(self, "ipv6_eibgp_maximum_paths")

    @property
    @pulumi.getter(name="ipv6EibgpMaximumPathsVariable")
    def ipv6_eibgp_maximum_paths_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "ipv6_eibgp_maximum_paths_variable")

    @property
    @pulumi.getter(name="ipv6Neighbors")
    def ipv6_neighbors(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv6NeighborResult']:
        """
        Set BGP IPv6 neighbors
        """
        return pulumi.get(self, "ipv6_neighbors")

    @property
    @pulumi.getter(name="ipv6Networks")
    def ipv6_networks(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv6NetworkResult']:
        """
        Configure the networks for BGP to advertise
        """
        return pulumi.get(self, "ipv6_networks")

    @property
    @pulumi.getter(name="ipv6Originate")
    def ipv6_originate(self) -> bool:
        """
        BGP Default Information Originate
        """
        return pulumi.get(self, "ipv6_originate")

    @property
    @pulumi.getter(name="ipv6OriginateVariable")
    def ipv6_originate_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "ipv6_originate_variable")

    @property
    @pulumi.getter(name="ipv6Redistributes")
    def ipv6_redistributes(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelIpv6RedistributeResult']:
        """
        Redistribute routes into BGP
        """
        return pulumi.get(self, "ipv6_redistributes")

    @property
    @pulumi.getter(name="ipv6TableMapFilter")
    def ipv6_table_map_filter(self) -> bool:
        """
        Table map filtered or not
        """
        return pulumi.get(self, "ipv6_table_map_filter")

    @property
    @pulumi.getter(name="ipv6TableMapFilterVariable")
    def ipv6_table_map_filter_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "ipv6_table_map_filter_variable")

    @property
    @pulumi.getter(name="ipv6TableMapRoutePolicyId")
    def ipv6_table_map_route_policy_id(self) -> str:
        return pulumi.get(self, "ipv6_table_map_route_policy_id")

    @property
    @pulumi.getter(name="keepaliveTime")
    def keepalive_time(self) -> int:
        """
        Interval (seconds) of keepalive messages sent to its BGP peer
        """
        return pulumi.get(self, "keepalive_time")

    @property
    @pulumi.getter(name="keepaliveTimeVariable")
    def keepalive_time_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "keepalive_time_variable")

    @property
    @pulumi.getter(name="localRoutesDistance")
    def local_routes_distance(self) -> int:
        """
        Set administrative distance for local BGP routes
        """
        return pulumi.get(self, "local_routes_distance")

    @property
    @pulumi.getter(name="localRoutesDistanceVariable")
    def local_routes_distance_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "local_routes_distance_variable")

    @property
    @pulumi.getter(name="missingMedAsWorst")
    def missing_med_as_worst(self) -> bool:
        """
        If path has no MED, consider it to be worst path when selecting active BGP paths
        """
        return pulumi.get(self, "missing_med_as_worst")

    @property
    @pulumi.getter(name="missingMedAsWorstVariable")
    def missing_med_as_worst_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "missing_med_as_worst_variable")

    @property
    @pulumi.getter(name="mplsInterfaces")
    def mpls_interfaces(self) -> Sequence['outputs.GetTransportRoutingBgpProfileParcelMplsInterfaceResult']:
        """
        MPLS BGP Interface
        """
        return pulumi.get(self, "mpls_interfaces")

    @property
    @pulumi.getter(name="multipathRelax")
    def multipath_relax(self) -> bool:
        """
        Ignore AS for multipath selection
        """
        return pulumi.get(self, "multipath_relax")

    @property
    @pulumi.getter(name="multipathRelaxVariable")
    def multipath_relax_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "multipath_relax_variable")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the profile parcel
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="propagateAsPath")
    def propagate_as_path(self) -> bool:
        """
        Propagate AS Path
        """
        return pulumi.get(self, "propagate_as_path")

    @property
    @pulumi.getter(name="propagateAsPathVariable")
    def propagate_as_path_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "propagate_as_path_variable")

    @property
    @pulumi.getter(name="propagateCommunity")
    def propagate_community(self) -> bool:
        """
        Propagate Community
        """
        return pulumi.get(self, "propagate_community")

    @property
    @pulumi.getter(name="propagateCommunityVariable")
    def propagate_community_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "propagate_community_variable")

    @property
    @pulumi.getter(name="routerId")
    def router_id(self) -> str:
        """
        Configure BGP router identifier
        """
        return pulumi.get(self, "router_id")

    @property
    @pulumi.getter(name="routerIdVariable")
    def router_id_variable(self) -> str:
        """
        Variable name
        """
        return pulumi.get(self, "router_id_variable")

    @property
    @pulumi.getter
    def version(self) -> int:
        """
        The version of the profile parcel
        """
        return pulumi.get(self, "version")


class AwaitableGetTransportRoutingBgpProfileParcelResult(GetTransportRoutingBgpProfileParcelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransportRoutingBgpProfileParcelResult(
            always_compare_med=self.always_compare_med,
            always_compare_med_variable=self.always_compare_med_variable,
            as_number=self.as_number,
            as_number_variable=self.as_number_variable,
            compare_router_id=self.compare_router_id,
            compare_router_id_variable=self.compare_router_id_variable,
            description=self.description,
            deterministic_med=self.deterministic_med,
            deterministic_med_variable=self.deterministic_med_variable,
            external_routes_distance=self.external_routes_distance,
            external_routes_distance_variable=self.external_routes_distance_variable,
            feature_profile_id=self.feature_profile_id,
            hold_time=self.hold_time,
            hold_time_variable=self.hold_time_variable,
            id=self.id,
            internal_routes_distance=self.internal_routes_distance,
            internal_routes_distance_variable=self.internal_routes_distance_variable,
            ipv4_aggregate_addresses=self.ipv4_aggregate_addresses,
            ipv4_eibgp_maximum_paths=self.ipv4_eibgp_maximum_paths,
            ipv4_eibgp_maximum_paths_variable=self.ipv4_eibgp_maximum_paths_variable,
            ipv4_neighbors=self.ipv4_neighbors,
            ipv4_networks=self.ipv4_networks,
            ipv4_originate=self.ipv4_originate,
            ipv4_originate_variable=self.ipv4_originate_variable,
            ipv4_redistributes=self.ipv4_redistributes,
            ipv4_table_map_filter=self.ipv4_table_map_filter,
            ipv4_table_map_filter_variable=self.ipv4_table_map_filter_variable,
            ipv4_table_map_route_policy_id=self.ipv4_table_map_route_policy_id,
            ipv6_aggregate_addresses=self.ipv6_aggregate_addresses,
            ipv6_eibgp_maximum_paths=self.ipv6_eibgp_maximum_paths,
            ipv6_eibgp_maximum_paths_variable=self.ipv6_eibgp_maximum_paths_variable,
            ipv6_neighbors=self.ipv6_neighbors,
            ipv6_networks=self.ipv6_networks,
            ipv6_originate=self.ipv6_originate,
            ipv6_originate_variable=self.ipv6_originate_variable,
            ipv6_redistributes=self.ipv6_redistributes,
            ipv6_table_map_filter=self.ipv6_table_map_filter,
            ipv6_table_map_filter_variable=self.ipv6_table_map_filter_variable,
            ipv6_table_map_route_policy_id=self.ipv6_table_map_route_policy_id,
            keepalive_time=self.keepalive_time,
            keepalive_time_variable=self.keepalive_time_variable,
            local_routes_distance=self.local_routes_distance,
            local_routes_distance_variable=self.local_routes_distance_variable,
            missing_med_as_worst=self.missing_med_as_worst,
            missing_med_as_worst_variable=self.missing_med_as_worst_variable,
            mpls_interfaces=self.mpls_interfaces,
            multipath_relax=self.multipath_relax,
            multipath_relax_variable=self.multipath_relax_variable,
            name=self.name,
            propagate_as_path=self.propagate_as_path,
            propagate_as_path_variable=self.propagate_as_path_variable,
            propagate_community=self.propagate_community,
            propagate_community_variable=self.propagate_community_variable,
            router_id=self.router_id,
            router_id_variable=self.router_id_variable,
            version=self.version)


def get_transport_routing_bgp_profile_parcel(feature_profile_id: Optional[str] = None,
                                             id: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransportRoutingBgpProfileParcelResult:
    """
    This data source can read the Transport Routing BGP profile parcel.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_transport_routing_bgp_profile_parcel(id="f6b2c44c-693c-4763-b010-895aa3d236bd",
        feature_profile_id="f6dd22c8-0b4f-496c-9a0b-6813d1f8b8ac")
    ```


    :param str feature_profile_id: Feature Profile ID
    :param str id: The id of the profile parcel
    """
    __args__ = dict()
    __args__['featureProfileId'] = feature_profile_id
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sdwan:index/getTransportRoutingBgpProfileParcel:getTransportRoutingBgpProfileParcel', __args__, opts=opts, typ=GetTransportRoutingBgpProfileParcelResult).value

    return AwaitableGetTransportRoutingBgpProfileParcelResult(
        always_compare_med=pulumi.get(__ret__, 'always_compare_med'),
        always_compare_med_variable=pulumi.get(__ret__, 'always_compare_med_variable'),
        as_number=pulumi.get(__ret__, 'as_number'),
        as_number_variable=pulumi.get(__ret__, 'as_number_variable'),
        compare_router_id=pulumi.get(__ret__, 'compare_router_id'),
        compare_router_id_variable=pulumi.get(__ret__, 'compare_router_id_variable'),
        description=pulumi.get(__ret__, 'description'),
        deterministic_med=pulumi.get(__ret__, 'deterministic_med'),
        deterministic_med_variable=pulumi.get(__ret__, 'deterministic_med_variable'),
        external_routes_distance=pulumi.get(__ret__, 'external_routes_distance'),
        external_routes_distance_variable=pulumi.get(__ret__, 'external_routes_distance_variable'),
        feature_profile_id=pulumi.get(__ret__, 'feature_profile_id'),
        hold_time=pulumi.get(__ret__, 'hold_time'),
        hold_time_variable=pulumi.get(__ret__, 'hold_time_variable'),
        id=pulumi.get(__ret__, 'id'),
        internal_routes_distance=pulumi.get(__ret__, 'internal_routes_distance'),
        internal_routes_distance_variable=pulumi.get(__ret__, 'internal_routes_distance_variable'),
        ipv4_aggregate_addresses=pulumi.get(__ret__, 'ipv4_aggregate_addresses'),
        ipv4_eibgp_maximum_paths=pulumi.get(__ret__, 'ipv4_eibgp_maximum_paths'),
        ipv4_eibgp_maximum_paths_variable=pulumi.get(__ret__, 'ipv4_eibgp_maximum_paths_variable'),
        ipv4_neighbors=pulumi.get(__ret__, 'ipv4_neighbors'),
        ipv4_networks=pulumi.get(__ret__, 'ipv4_networks'),
        ipv4_originate=pulumi.get(__ret__, 'ipv4_originate'),
        ipv4_originate_variable=pulumi.get(__ret__, 'ipv4_originate_variable'),
        ipv4_redistributes=pulumi.get(__ret__, 'ipv4_redistributes'),
        ipv4_table_map_filter=pulumi.get(__ret__, 'ipv4_table_map_filter'),
        ipv4_table_map_filter_variable=pulumi.get(__ret__, 'ipv4_table_map_filter_variable'),
        ipv4_table_map_route_policy_id=pulumi.get(__ret__, 'ipv4_table_map_route_policy_id'),
        ipv6_aggregate_addresses=pulumi.get(__ret__, 'ipv6_aggregate_addresses'),
        ipv6_eibgp_maximum_paths=pulumi.get(__ret__, 'ipv6_eibgp_maximum_paths'),
        ipv6_eibgp_maximum_paths_variable=pulumi.get(__ret__, 'ipv6_eibgp_maximum_paths_variable'),
        ipv6_neighbors=pulumi.get(__ret__, 'ipv6_neighbors'),
        ipv6_networks=pulumi.get(__ret__, 'ipv6_networks'),
        ipv6_originate=pulumi.get(__ret__, 'ipv6_originate'),
        ipv6_originate_variable=pulumi.get(__ret__, 'ipv6_originate_variable'),
        ipv6_redistributes=pulumi.get(__ret__, 'ipv6_redistributes'),
        ipv6_table_map_filter=pulumi.get(__ret__, 'ipv6_table_map_filter'),
        ipv6_table_map_filter_variable=pulumi.get(__ret__, 'ipv6_table_map_filter_variable'),
        ipv6_table_map_route_policy_id=pulumi.get(__ret__, 'ipv6_table_map_route_policy_id'),
        keepalive_time=pulumi.get(__ret__, 'keepalive_time'),
        keepalive_time_variable=pulumi.get(__ret__, 'keepalive_time_variable'),
        local_routes_distance=pulumi.get(__ret__, 'local_routes_distance'),
        local_routes_distance_variable=pulumi.get(__ret__, 'local_routes_distance_variable'),
        missing_med_as_worst=pulumi.get(__ret__, 'missing_med_as_worst'),
        missing_med_as_worst_variable=pulumi.get(__ret__, 'missing_med_as_worst_variable'),
        mpls_interfaces=pulumi.get(__ret__, 'mpls_interfaces'),
        multipath_relax=pulumi.get(__ret__, 'multipath_relax'),
        multipath_relax_variable=pulumi.get(__ret__, 'multipath_relax_variable'),
        name=pulumi.get(__ret__, 'name'),
        propagate_as_path=pulumi.get(__ret__, 'propagate_as_path'),
        propagate_as_path_variable=pulumi.get(__ret__, 'propagate_as_path_variable'),
        propagate_community=pulumi.get(__ret__, 'propagate_community'),
        propagate_community_variable=pulumi.get(__ret__, 'propagate_community_variable'),
        router_id=pulumi.get(__ret__, 'router_id'),
        router_id_variable=pulumi.get(__ret__, 'router_id_variable'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_transport_routing_bgp_profile_parcel)
def get_transport_routing_bgp_profile_parcel_output(feature_profile_id: Optional[pulumi.Input[str]] = None,
                                                    id: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransportRoutingBgpProfileParcelResult]:
    """
    This data source can read the Transport Routing BGP profile parcel.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sdwan as sdwan

    example = sdwan.get_transport_routing_bgp_profile_parcel(id="f6b2c44c-693c-4763-b010-895aa3d236bd",
        feature_profile_id="f6dd22c8-0b4f-496c-9a0b-6813d1f8b8ac")
    ```


    :param str feature_profile_id: Feature Profile ID
    :param str id: The id of the profile parcel
    """
    ...
