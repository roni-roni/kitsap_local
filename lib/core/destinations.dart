import 'package:flutter/material.dart';

/// Metadata for each top-level tab. Adding a tab (e.g. Jobs, someday) means:
/// one new enum value here + one new screen + one entry in `HomeShell`.
enum AppTab {
  bus(
    label: 'Bus',
    icon: Icons.directions_bus_outlined,
    selectedIcon: Icons.directions_bus,
    arrivesInClass: 6,
    blurb: 'Kitsap Transit routes and stops on a map, plus live positions.',
    dataSources: [
      'Kitsap Transit GTFS feed (static routes, stops, shapes)',
      'OneBusAway Puget Sound API (real-time, key required)',
      'Kitsap Transit BusTime (real-time, access pending)',
    ],
  ),
  ferry(
    label: 'Ferry',
    icon: Icons.directions_boat_outlined,
    selectedIcon: Icons.directions_boat,
    arrivesInClass: 3,
    blurb: 'Terminals, next departures, schedules, and service alerts.',
    dataSources: [
      'WSDOT Ferries Schedule + Terminals APIs (access code required)',
    ],
  ),
  government(
    label: 'Government',
    icon: Icons.account_balance_outlined,
    selectedIcon: Icons.account_balance,
    arrivesInClass: 5,
    blurb: 'Meetings, elected officials, and how to report an issue.',
    dataSources: [
      'Kitsap County officials table (HTML, via tools/county_officials.py)',
      'City council calendars (Bremerton, Bainbridge Island, Port Orchard, Poulsbo)',
      'SeeClickFix and county web forms (link-outs)',
    ],
  ),
  parks(
    label: 'Parks',
    icon: Icons.park_outlined,
    selectedIcon: Icons.park,
    arrivesInClass: 3,
    blurb: 'City, county, state, DNR, and federal land open to the public.',
    dataSources: [
      'Kitsap County GIS open data (park locations and boundaries)',
      'WA State Parks / DNR open data',
      'Discover Pass rules (state parks and DNR lands)',
    ],
  ),
  events(
    label: 'Events',
    icon: Icons.event_outlined,
    selectedIcon: Icons.event,
    arrivesInClass: 5,
    blurb: 'What is happening around the county and its cities.',
    dataSources: [
      'Hand-curated data/events.json (v1)',
      'County and city calendars (feeds, if any, later)',
    ],
  ),
  help(
    label: 'Help',
    icon: Icons.volunteer_activism_outlined,
    selectedIcon: Icons.volunteer_activism,
    arrivesInClass: 4,
    blurb: 'Volunteer opportunities, organized by need or interest.',
    dataSources: ['Hand-curated data/help.json'],
  );

  const AppTab({
    required this.label,
    required this.icon,
    required this.selectedIcon,
    required this.arrivesInClass,
    required this.blurb,
    required this.dataSources,
  });

  /// Short on purpose: six labels must fit on a phone-width bar.
  final String label;
  final IconData icon;
  final IconData selectedIcon;

  /// The class in which this tab first gets real content.
  final int arrivesInClass;
  final String blurb;
  final List<String> dataSources;
}
