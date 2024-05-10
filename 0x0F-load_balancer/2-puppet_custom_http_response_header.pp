nginx::resource::server { 'example.com':
  listen_port => 80,
  proxy       => 'http://backend',
  add_header  => {
    'X-Custom-Header' => 'custom-value',
  },
}
